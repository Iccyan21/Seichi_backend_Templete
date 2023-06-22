from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Customer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Customer
from .serializers import CustomerSerializer
from post.models import Post
from urllib.parse import unquote

def index(request):
    template = loader.get_template('gmap/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def hello(request):
    return render(request, 'gmap/hello.html')

def parace(request,name):   
    Candidate_data = get_object_or_404(Customer, name=name)
    params = {
        'Candidate_data': Candidate_data,
    }
    return render(request,'gmap/prace.html',params)


class CandidateDataAPI(APIView):
    def get_queryset(self):
        return Customer.objects.all()

    def get(self, request, name):
        try:
            customer = self.get_queryset().get(name=name)
            serializer = CustomerSerializer(customer)
            data = serializer.data
            data['image'] = unquote(data['image'])
            return Response(data)
            
        except Customer.DoesNotExist:
            return Response(status=404)


class CandidateDataIntAPI(APIView):
    def get_queryset(self):
        return Customer.objects.all()

    def get(self, request, animeid):
        try:
            customer = self.get_queryset().filter(animeid=animeid)
            serializer = CustomerSerializer(customer, many=True)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(status=404)



def prace_detail(request, name):
    prace = get_object_or_404(Customer, name=name)
    posts = Post.objects.filter(PraceID=prace)
    context = {
        'prace': prace,
        'posts': posts
    }
    return render(request, 'gmap/prace_detail.html', context)


def search_customers(request):
    query = request.GET.get('q', '')
    customers = Customer.objects.filter(name__icontains=query)
    return render(request, 'gmap/search_results.html', {'customers': customers, 'query': query})


class CustomerSearchAPIView(APIView):    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Customer.objects.search_by_name(query)

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)