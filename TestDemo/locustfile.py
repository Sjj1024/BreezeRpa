from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        # self.client.get("https://www.baidu.com/")
        self.client.get("https://www.jianshu.com")
