#views.py

@api_view(['GET' ])
def test(request):
    try:
        supp = supplier.objects.all()
        serializerr = testserializer(supp , many = True)
        return Response(serializerr.data)
    except Exception as e:
        return JsonResponse({"error":str(e)})
    
#serializer
class testserializer(ModelSerializer):
	class Meta:
		model = supplier
		fields = ['name',]
