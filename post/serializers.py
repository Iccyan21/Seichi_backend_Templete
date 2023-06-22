from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Post
        fields = ['PraceID_id','UserID','PraceID','AnimeID','title', 'content', 'created_at']