from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2.5)

    @task
    def hello_world(self):
        self.client.get('/home')
        self.client.get('/user/data')
        self.client.put('/user/data')
        self.client.post('/attendance/time')
        self.client.post('/attendance/days')
        self.client.get('/attendance')