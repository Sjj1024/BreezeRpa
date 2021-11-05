import stomp

# __listener_name = 'SampleListener'
__queue_name = ''
__topic_name = '/topic/IOT_THIRD_WARN'

# __host = "60.191.78.86"
# __port = 8184
# __user = 'thrid'
# __password = 'thrid123'

__host = "127.0.0.1"
__port = 61613
__user = 'admin'
__password = 'admin'


def send_to_queue(msg):
    conn = stomp.Connection10([(__host, __port)])
    conn.connect(wait=True)
    conn.send('SampleQueue', msg)
    conn.disconnect()


def send_to_topic(topic_name, msg):
    conn = stomp.Connection10([(__host, __port)], reconnect_attempts_max=-1)
    conn.connect(wait=True)
    conn.send(topic_name, msg)
    conn.disconnect()


if __name__ == '__main__':
    send_to_queue('sample queue222')
    send_to_topic(__topic_name, '{"name":"sjj"}')
