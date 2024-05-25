from rest_framework.decorators import api_view
from api_app.models import Produto
from api_app.models import Nivel
from api_app.models import Relacao
from api_app.serializers import ProdutoSerializer
from api_app.serializers import NivelSerializer
from api_app.serializers import RelacaoSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()

        serializer = ProdutoSerializer(produtos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def produto(request, id):
    try:
        produto = Produto.objects.get(id=id)
    except Produto.DoesNotExist:
        return Response({'message': 'Produto does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        produto.delete()
        return Response({'message': 'Produto deleted.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def niveis(request):
    if request.method == 'GET':
        niveis = Nivel.objects.all()

        serializer = NivelSerializer(niveis, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = NivelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def nivel(request, id):
    try:
        nivel = Nivel.objects.get(id=id)
    except Nivel.DoesNotExist:
        return Response({'message': 'Nivel does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NivelSerializer(nivel)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = NivelSerializer(nivel, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        nivel.delete()
        return Response({'message': 'Nivel deleted.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def relacoes(request):
    if request.method == 'GET':
        relacoes = Relacao.objects.all()

        serializer = RelacaoSerializer(relacoes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = RelacaoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def relacao(request, id):
    try:
        relacao = Relacao.objects.get(id=id)
    except Relacao.DoesNotExist:
        return Response({'message': 'Relacao does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RelacaoSerializer(relacao)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = RelacaoSerializer(relacao, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        relacao.delete()
        return Response({'message': 'Relacao deleted.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)