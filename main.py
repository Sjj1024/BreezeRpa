import stomp
import time


class LocalConst:
    mq_host = [('60.191.78.86', 8182)]
    mq_user = 'thrid'
    mq_password = 'thrid123'
    mq_topic = 'IOT_THIRD_WARN'
    mq_listener_name = 'MdtListener'


class MdtListener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


class MdtReceive:

    def __init__(self):
        self.conn = stomp.StompConnection10(host_and_ports=LocalConst.mq_host)

    def receive_from_topic(self):
        self.conn.set_listener(LocalConst.mq_listener_name, MdtListener())
        self.conn.connect(LocalConst.mq_user, LocalConst.mq_password, wait=True)
        # self.conn.subscribe(destination=LocalConst.mq_topic, id='1')
        self.conn.send(destination=LocalConst.mq_topic, body='')


if __name__ == '__main__':
    mdt_rec = MdtReceive()
    mdt_rec.receive_from_topic()
