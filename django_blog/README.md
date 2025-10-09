# Django Blog App

## Features
- Users can **view all posts** (public access)
- Only **logged-in users** can create posts
- Only **the author** of a post can edit or delete it

## Permissions
- `LoginRequiredMixin` ensures only authenticated users can create, update, or delete posts.
- `UserPassesTestMixin` ensures only the post’s author can modify or remove it.

## Views
- `PostListView` — shows all posts
- `PostDetailView` — shows individual post
- `PostCreateView` — allows post creation (login required)
- `PostUpdateView` — allows editing (author only)
- `PostDeleteView` — allows deletion (author only)

## Testing
- Check that unauthorized users are redirected to login
- Ensure users can only edit or delete their own posts
