import os

def generate_secret_key():
    return os.urandom(24).hex()

def update_env_file(secret_key, env_file_path):
    with open(env_file_path, 'r') as file:
        lines = file.readlines()

    with open(env_file_path, 'w') as file:
        for line in lines:
            if line.startswith("SECRET_KEY="):
                file.write(f"SECRET_KEY=\"{secret_key}\"\n")
            else:
                file.write(line)

if __name__ == "__main__":
    secret_key = generate_secret_key()
    env_file_path = '.env'  # Adjust the path if your .env file is located elsewhere
    update_env_file(secret_key, env_file_path)
    print(f"SECRET_KEY has been updated in {env_file_path}")