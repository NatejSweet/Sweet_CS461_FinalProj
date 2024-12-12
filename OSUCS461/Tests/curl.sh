#!/bin/bash

BASE_URL="http://127.0.0.1:8855/v1"

# Create a new user
echo "Creating a new user..."
res=$(curl -s -X POST "$BASE_URL/users" -H "Content-Type: application/json" -d '{
  "name": "newuser",
  "time_created" : 2
}')
expected_response='{"uuid":"2e42fb99dfb563d785e3888fd2ceb14c","name":"newuser","time_created":2}'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"

uuid=$(echo $res | jq -r '.uuid')

# # Get a specific user by ID
echo "Getting user with ID $uuid..."
res=$(curl -s -X GET "$BASE_URL/users/$uuid")
expected_response='{"uuid":"2e42fb99dfb563d785e3888fd2ceb14c","name":"newuser","time_created":2}'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"

# # Get all users
echo "Getting all users..."
res=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$BASE_URL/users")
if [ "$res" -eq 200 ]; then
    echo "Test Passed"
else
    echo "Test Failed"
fi

# Ensure the response has content
res=$(curl -s -X GET "$BASE_URL/users")
if [ -n "$res" ]; then
    echo "Response has content"
else
    echo "Response is empty"
fi
echo $res
echo "\n"

# # Update a user by ID
echo "Updating user with ID $uuid..."
res=$(curl -s -X PUT "$BASE_URL/users/$uuid" -H "Content-Type: application/json" -d '{
  "name": "updateduser"
}')
expected_response='{"uuid":"2e42fb99dfb563d785e3888fd2ceb14c","name":"updateduser","time_created":2}'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"
# Delete a user by ID
echo "Deleting user with ID $uuid..."
res=$(curl -s -X DELETE "$BASE_URL/users/$uuid")
expected_response='{"message":"User deleted"}'
echo $res
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"

# Create a new post
echo "Creating a new post..."
res=$(curl -s -X POST "$BASE_URL/posts" -H "Content-Type: application/json" -d '{
  "user_uuid": "2e42fb99dfb563d785e3888fd2ceb14c",
  "post_9char": "post12345",
  "text": "This is a new post",
  "time_created": 1633024800
}')
expected_response='{"user_uuid":"2e42fb99dfb563d785e3888fd2ceb14c","post_9char":"post12345","text":"This is a new post","time_created":1633024800,"uuid":"08193eea5eaf516c30cf72b1bf6aad37"}'

if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"
post_uuid=$(echo $res | jq -r '.uuid')


# # Get a specific post by ID
echo "Getting post with ID $post_uuid..."
res=$(curl -s -X GET "$BASE_URL/posts/$post_uuid")
expected_response='{"uuid":"08193eea5eaf516c30cf72b1bf6aad37","user_uuid":"2e42fb99dfb563d785e3888fd2ceb14c","post_9char":"post12345","text":"This is a new post","time_created":1633024800}'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"

# # Update a post by ID
echo "Updating post with ID $post_uuid..."
res=$(curl -s -X PUT "$BASE_URL/posts/$post_uuid" -H "Content-Type: application/json" -d '{
  "user_uuid": "2e42fb99dfb563d785e3888fd2ceb14c",
  "post_9char": "post12345",
  "text": "This is an updated post",
  "time_created": 1633024800
}')
expected_response='{"uuid":"08193eea5eaf516c30cf72b1bf6aad37","user_uuid":"2e42fb99dfb563d785e3888fd2ceb14c","post_9char":"post12345","text":"This is an updated post","time_created":1633024800}'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"

# Get all posts for a specific user
echo "Getting all posts for user with ID $uuid..."
res=$(curl GET -s "$BASE_URL/users/$uuid/posts")
expected_response='[{"uuid":"08193eea5eaf516c30cf72b1bf6aad37","user_uuid":"2e42fb99dfb563d785e3888fd2ceb14c","post_9char":"post12345","text":"This is an updated post","time_created":1633024800}]'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"

# Delete a post by ID
echo "Deleting post with ID $POST_ID..."
res=$(curl -s -X DELETE "$BASE_URL/posts/$post_uuid")
expected_response='{"message":"Post deleted"}'
if [ "$res" = "$expected_response" ]; then
  echo "Test Passed"
else
  echo "Test Failed"
fi
echo $res
echo "\n"
