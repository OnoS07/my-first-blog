from django.shortcuts import render
from django.utils import timezone
from .models import Post
#models.pyからPostモデルを読み込んで、こっちでも使えるようにする
from django.shortcuts import render, get_object_or_404


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#lte は less than or equal to で現在時刻より前に作られたデータを抽出
	#公開時刻順で、Postモデルのobjectsをpost変数に代入。これでモデル → ビュー のデータ渡しはできた
	return render(request, 'blog/post_list.html', {'posts': posts})
    #"posts"という名前で、post変数を html(テンプレート)側へ渡す

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})