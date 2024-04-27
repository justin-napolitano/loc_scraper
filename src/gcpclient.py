from google.cloud import storage
import os

class GCSClient:
    def __init__(self, project_id, credentials_path=None):
        """
        Initializes the Google Cloud Storage client.

        Args:
            project_id (str): The Google Cloud project ID.
            credentials_path (str, optional): Path to the JSON file containing service account credentials.
                                              If not provided, it will use the default credentials from the environment.
        """
        self.project_id = project_id
        self.credentials_path = credentials_path
        self.client = self._create_client()

    def _create_client(self):
        """
        Creates and returns the Google Cloud Storage client.

        Returns:
            google.cloud.storage.Client: The initialized Google Cloud Storage client.
        """
        if self.credentials_path:
            client = storage.Client.from_service_account_json(self.credentials_path)
        else:
            client = storage.Client(project=self.project_id)
        return client

    def list_buckets(self):
        """
        Lists all buckets in the Google Cloud Storage project.

        Returns:
            list: A list of bucket names.
        """
        buckets = [bucket.name for bucket in self.client.list_buckets()]
        return buckets

# Example usage:

def test():

    project_id = os.environ.get("GCPPROJECTID")
    # credentials_path = "path/to/your/credentials.json"  # Optional if using default credentials
    gcs = GCSClient(project_id, credentials_path=None)

    # List buckets
    buckets = gcs.list_buckets()
    print("Buckets:", buckets)

if __name__ == "__main__":
    test()

