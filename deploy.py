import os
import subprocess
import sys

def create_virtual_env():
    print("Создается виртуальное окружение...")
    subprocess.run([sys.executable, '-m', 'venv', 'myenv'])

def install_requirements():
    print("Устанавливаются зависимости...")
    # На Windows и Unix пути к pip разные, определяем:
    pip_executable = os.path.join('myenv', 'Scripts', 'pip') if os.name == 'nt' else os.path.join('myenv', 'bin', 'pip')
    subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])

def run_application():
    print("Запускается приложение...")
    # На Windows и Unix пути к python разные, определяем:
    python_executable = os.path.join('myenv', 'Scripts', 'python') if os.name == 'nt' else os.path.join('myenv', 'bin', 'python')
    subprocess.Popen([python_executable, 'main.py'])

def main():
    if os.path.exists('myenv'):
        run_application()
    else:
        create_virtual_env()
        install_requirements()
        run_application()

if __name__ == '__main__':
    main()
