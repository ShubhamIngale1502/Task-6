from rest_framework.views import APIView
from  rest_framework.response import Response
from  .models import Product
from .serializer import ProductSerializer
import pandas as  pd
from django.shortcuts import get_object_or_404

class Uploadfile(APIView):
    
    def post(self,request):
        try:
            input_file = request.data.get('file')
            obj = pd.read_excel(input_file)
            obj.dropna(how='all', axis=1, inplace=True)
            if 'product_manufacturing_date' in obj.columns:
                obj['product_manufacturing_date'] = obj['product_manufacturing_date'].dt.date
            data_list = obj.to_dict(orient='records')
            serializer = ProductSerializer(data=data_list, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data,status=205)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors,status=400)
        
    def get(self,request):
        try:
            obj = Product.objects.all()
            serializer = ProductSerializer(obj,many=True)
            return Response(data=serializer.data,status=200)
        except:
            return Response(data=serializer.errors,status=400)
        
class Details(APIView):
    
    def get(self,request,pk):
        try:
            obj = get_object_or_404(Product,pk=pk)
            serializer = ProductSerializer(obj)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'Getting Error In Featching Data'})
    def put(self,request,pk):
        try:
            obj = get_object_or_404(Product,pk=pk)
            serializer = ProductSerializer(data=request.data,instance=obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data,status=205)
        except:
            return Response(data=serializer.errors,status=400) 
    
    def patch(self, request, pk):
        try:
            obj = get_object_or_404(Product,pk=pk)
            serializer = ProductSerializer(data=request.data,instance=obj,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data,status=205)
        except:
            return Response(data=serializer.errors,status=400) 
    
    def delete(self,request,pk):

            obj = get_object_or_404(Product,pk=pk)
            obj.delete()
            return Response(data=None,status=204)    
    
    
        

            


