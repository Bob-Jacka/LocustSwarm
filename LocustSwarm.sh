# shellcheck disable=SC1009

python LocustSwarm --web_ui_port=8089 \
            --web_ui_address='127.0.0.1' \
            --strategy=peak \
            --locust_start_count=10

            #locust_start_count - optional parameter
            #peak \ ramp-up \ sustain-load