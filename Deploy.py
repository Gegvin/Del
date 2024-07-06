import os
import subprocess
import sys

def create_virtual_env():
    print("Создается виртуальное окружение...")
    subprocess.run([sys.executable, '-m', 'venv', 'myenv'])

def install_requirements():
    print("Устанавливаются зависимости...")
    # На Windows и Unix пути к pip разные, определим это:
    pip_executable = os.path.join('myenv', 'Scripts', 'pip') if os.name == 'nt' else os.path.join('myenv', 'bin', 'pip')
    subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])

def run_application():
    print("Запускается приложение...")
    # На Windows и Unix пути к python разные, определим это:
    python_executable = os.path.join('myenv', 'Scripts', 'python') if os.name == 'nt' else os.path.join('myenv', 'bin', 'python')
    subprocess.Popen([python_executable, 'app.py'])

def main():
    create_virtual_env()
    install_requirements()
    run_application()

if __name__ == '__main__':
    main()