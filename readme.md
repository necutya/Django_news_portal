# Django news portal

#### Deployment link
[Django news portal] (https://djangonewsplatform.herokuapp.com)

## Small documentaton
What can you do in this app: 
+ Show all posts and comments to them
+ Register / Login
+ Create a post (if you are authenticated) 
+ Update / delete post (if you are an owner of this post)
+ Create a commet to a post (if you are authenticated)
+ Update / delete comment (if you are an owner of this post)
+ Using API to all things, which has been mentioned below

## API
[Link to the embeded Postman collection](https://www.getpostman.com/collections/cc2288f0b73ed0840d04) 

Django news portal provides user friendly REST API. There are some  

| API | What can you do|
|<url>/api/auth/token| See all posts |
|<url>/api/posts| See all posts |
|<url>/api/comments| See all comments |
|<url>/api/posts/<int: post_id>| See a post with id |
|<url>/api/comments/<int: comment_id>| See a comment with id |
|<url>/api/posts/<int: post_id>/update| Update a post with id |
|<url>/api/comments/<int: comment_id>/update| Update a comment with id |
|<url>/api/posts/<int: post_id>/delete| Delete a post with id |
|<url>/api/comments/<int: comment_id>/delete| Delete a comment with id |
 
 
 
