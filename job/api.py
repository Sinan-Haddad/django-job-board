# ## views 

# from .models import Job
# from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


# @api_view(['GET'])
from job.models import Job
from job.serializers import JobSerializer

@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data':data})
    
@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})

# class JobListApi(generics.ListAPIView):
#     model=Job
#     queryset = Job.objects.all()
#     serializer_class=JobSerializer


class JobListApi(generics.ListCreateAPIView):
    model=Job
    queryset = Job.objects.all()
    serializer_class=JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    model=Job

    serializer_class=JobSerializer
    queryset = Job.objects.all()
    lookup_field='id'


