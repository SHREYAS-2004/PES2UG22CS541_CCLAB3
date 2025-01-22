from locust import task, run_single_user
from locust import FastHttpUser


class browse(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/browse",
            headers=self.default_headers,  # Use default_headers here to reduce redundancy
            catch_response=True,
        ) as resp:
            if resp.status_code == 200:
                resp.success()  # Mark it as a success if the response is 200
            else:
                resp.failure(f"Request failed with status {resp.status_code}")  # Handle failure

if __name__ == "__main__":
    run_single_user(browse)
