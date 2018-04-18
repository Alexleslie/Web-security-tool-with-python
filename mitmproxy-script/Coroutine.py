from mitmproxy import eventsequence
import gevent
import gevent.monkey

gevent.monkey.patch_all()

def tornado(fn):
    def _tornado(obj):
        def run():
            fn(obj)
            if obj.reply.state == "taken":
                if not obj.reply.has_message:
                    obj.reply.ack()
                obj.reply.commit()
            obj.reply.take()
        t1 = gevent.spawn(run)
        t1.join()
        #ScriptThread(
        #    "script.concurrent (%s)" % fn.__name__,
        #    target=run
        #).start()
        # Support @concurrent for class-based addons

        return _tornado   
