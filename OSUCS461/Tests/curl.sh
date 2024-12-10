#!/bin/bash

BASE_URL="http://127.0.0.1:8855/v1"

# Create a new user
echo "Creating a new user..."
curl -X POST "$BASE_URL/users" -H "Content-Type: application/json" -d '{
  "name": "newuser",
  "time_created": 1633024800
# }'
# echo -e "\n"
# # Get all users
# echo "Getting all users..."
# curl -X GET "$BASE_URL/users"
# echo -e "\n"

# # Get a specific user by ID
# USER_ID=1
# echo "Getting user with ID $USER_ID..."
# curl -X GET "$BASE_URL/users/$USER_ID"
# echo -e "\n"



# # Update a user by ID
# echo "Updating user with ID $USER_ID..."
# curl -X PUT "$BASE_URL/users/$USER_ID" -H "Content-Type: application/json" -d '{
#   "username": "updateduser"
# }'
# echo -e "\n"

# # Delete a user by ID
# echo "Deleting user with ID $USER_ID..."
# curl -X DELETE "$BASE_URL/users/$USER_ID"
# echo -e "\n"

# # Get all posts
# echo "Getting all posts..."
# curl -X GET "$BASE_URL/posts"
# echo -e "\n"

# # Get a specific post by ID
# POST_ID=1
# echo "Getting post with ID $POST_ID..."
# curl -X GET "$BASE_URL/posts/$POST_ID"
# echo -e "\n"

# # Create a new post
# echo "Creating a new post..."
# curl -X POST "$BASE_URL/posts" -H "Content-Type: application/json" -d '{
#   "user_uuid": "user-uuid",
#   "post_9char": "post12345",
#   "text": "This is a new post",
#   "time_created": 1633024800
# }'
# echo -e "\n"

# # Update a post by ID
# echo "Updating post with ID $POST_ID..."
# curl -X PUT "$BASE_URL/posts/$POST_ID" -H "Content-Type: application/json" -d '{
#   "text": "Updated post text"
# }'
# echo -e "\n"

# # Delete a post by ID
# echo "Deleting post with ID $POST_ID..."
# curl -X DELETE "$BASE_URL/posts/$POST_ID"
# echo -e "\n"

# # Get all posts for a specific user
# echo "Getting all posts for user with ID $USER_ID..."
# curl -X GET "$BASE_URL/users/$USER_ID/posts"
# echo -e "\n"