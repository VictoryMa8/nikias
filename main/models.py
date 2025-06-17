from django.db import models
from django.contrib.auth.models import User # Used for the profile model
from django.core.validators import URLValidator 
from django.db.models.signals import post_save # Signal used for creating a profile when a user is created
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    '''
    Extends the built in user model with Nikias-specific fields
    One-to-one relationship, so each User has exactly one profile
    Fields: user, bio, avatar, created_at, ...(more coming soon)
    '''

    # One user is connected to one profile
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, # If a user is deleted, their profile is deleted as well
        related_name='profile'
    )

    # Biography of the user
    bio = models.TextField(
        max_length=500, 
        blank=True,
        help_text="A simple description of the user on their profile"
    )
    
    # An avatar (image) that the user can upload to their profile
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text="A profile picture of the user"
    )
    
    # When the user was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """String representation of the model - shows in admin interface"""
        return f"{self.user.username}'s Profile"
    
    # Function to view all accepted friend requests
    def view_accepted(self):
        friends = Profile.objects.filter(
            # Query for sent and received friend requests
            models.Q(
                sent_friend_requests__sender=self, sent_friend_requests__status='A') |
            models.Q(
                received_friend_requests__receiver=self, received_friend_requests__status='A'))
        return friends
    
    # Function to view all pending friend requests
    def view_pending(self):
        return self.received_friend_requests.filter(status='P')
    
class Friendship(models.Model):
    '''
    Represents a friendship between two users
    When a friend request is accepted, a friendship instance is established
    '''

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('D', 'Declined'),  
    ]

    # User who sent the friend request
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sent_friend_requests'
    )

    # User who received the friend request
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='received_friend_requests'
    )

    # Status of the friendship
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='P'
    )

    # When the friend request was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Prevent duplicate friend requests
    class Meta:
        unique_together = ('sender', 'receiver')

    '''
    Function to accept the friend request and create relationship
    Explanation: user A sends a friend request to user B
    Creates a Friendship instance with sender=A and receiver=B
    User B can call accept() that marks the request as accepted ('A')
    Also creates their own instance where sender=B and receiver=A, also accepted
    '''
    def accept(self):
        self.status = 'A' # Mark friendship as accepted
        self.save()
        
        # Create the relationship for the other user if it doesn't exist
        reverse_relationship, created = Friendship.objects.get_or_create(
            sender=self.receiver, # Original receiver becomes sender
            receiver=self.sender,
            defaults={'status': 'A'}
        )

        if not created:
            reverse_relationship.status = 'A'
            reverse_relationship.save()
    
class Board(models.Model):
    '''
    A user can create a board which is blank at first, but can have posts added to it
    Fields: title, description, author, created_at
    '''

    # A title for the board
    title = models.CharField(max_length=100, help_text="A title for the board")

    # An optional description
    description = models.CharField(
        max_length=1000,
        blank=True,
        help_text="An optional description for the board"
    )

    # The author of the board
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='authored_boards' # Profiles have 'authored boards'
    )

    # When the board was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.user.username}"
    
class Post(models.Model):
    '''
    A user can create a post with a title, description, and image
    Fields: title, description, image, source, boards, and created_at
    '''

    # A title for the post
    title = models.CharField(max_length=100, help_text="A title for the post")

    # An optional description
    description = models.CharField(
        max_length=1000,
        blank=True,
        help_text="An optional description for the post"
    )

    # An image for the post
    image = models.ImageField(
        upload_to="posts/",
        help_text="An image for the post"
    )

    # The author of the post
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='authored_posts' # Profiles have 'authored posts'
    )

    # Source URL if post was saved from the web
    source = models.URLField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        help_text="The original source URL (optional)"
    )

    # Boards that this post can be found on (many-to-many)
    boards = models.ManyToManyField(
        Board,
        related_name="posts",
        blank=True
    )

    # When the post was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.user.username}"
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically create a profile when a user is created
    Every user should have a corresponding profile
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save a profile whenever the user is saved
    Keeps the profile in sync with any changes to the user
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        # Creates a profile if it doesn't exist
        Profile.objects.create(user=instance)