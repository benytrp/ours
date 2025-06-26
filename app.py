
from trinity_framework import TrinityWebsiteFramework

if __name__ == '__main__':
    framework = TrinityWebsiteFramework()
    framework.app.run(debug=True, host='0.0.0.0', port=5000)
