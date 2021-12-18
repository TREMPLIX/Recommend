from services.train import run
run()

from services.predict_top10 import run
run(1)

from services.add_new_user import run
run()

from services.update_user_ratings import run
run(1)
