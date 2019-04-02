import webserver.db_tool.hf_users as users
import webserver.db_tool.hf_restaurants as restaurants

# Reset eaters collection
users.update_users()

# Reset restaurants collection
restaurants.update()