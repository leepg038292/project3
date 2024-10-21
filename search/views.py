



# search/views.py

from django.shortcuts import render, get_object_or_404
from .models import Item
from django.core.paginator import Paginator
from django.http import JsonResponse

def item_list(request):
    query = request.GET.get('q', '')  # 검색어
    sort_option = request.GET.get('sort')  # 정렬 옵션

    items = Item.objects.all()

    # 검색 기능 추가 (향수 이름으로 검색)
    if query:
        items = items.filter(Name__icontains=query)  # 이름에 검색어가 포함된 항목 필터링

    # 정렬 기능 추가
    if sort_option == 'price':
        items = items.order_by('Price')  # 가격순 정렬
    elif sort_option == 'rate':
        items = items.order_by('Rate')  # 평점순 정렬

    paginator = Paginator(items, 30)  # 페이지당 30개 항목
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': page_obj, 'query': query})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # 아이템 상세 정보
    return render(request, 'product.html', {'item': item})



def top_first(request):
    top_item = Item.objects.first()  # 탑 제품
    items = Item.objects.all()  #탑 포함한 제품

    paginator = Paginator(items, 9)   # 9개로 페이지 네이션
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print({'top_item': top_item})
    return render(request, 'product.html', {'top_item': top_item,
                  'page_obj': page_obj})


def get_items_by_brand(request):
    brand_name = request.GET.get('brand', '')
    items = Item.objects.all()
    
    if brand_name:
        items = items.filter(Brand__icontains=brand_name)
        request.session['searched_brand'] = brand_name  # 세션에 브랜드 저장
        top_item = items.first()

    else:
        request.session['searched_brand'] = ''  # 검색 초기화
        top_item = items.first()
    
    
    
    # Pagination 설정
    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {
        'page_obj': page_obj, 
        'query': brand_name,
        'top_item': top_item
    })


from django.db.models import Q

from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
from django.db.models import Q

def filter_items(request):
    if request.method == 'GET':
        # 필터 조건 추출
        brand_name = request.GET.get('brand', '')
        price_range = request.GET.get('price_range', '')
        page = request.GET.get('page', 1)  # 페이지 번호

        # 모든 아이템 가져오기
        items = Item.objects.all()

        # 브랜드 필터링
        if brand_name:
            items = items.filter(Brand__icontains=brand_name)

        # 가격 범위에 따라 필터링 (여기서 items를 사용)
        if price_range == 'below100':
            items = items.filter(Price__lt=100000)  # 여기서 items를 사용
        elif price_range == 'below200':
            items = items.filter(Q(Price__gte=100000) & Q(Price__lt=200000))  # 여기서 items를 사용
        elif price_range == 'above200':
            items = items.filter(Price__gte=200000)  # 여기서 items를 사용

        # JSON 응답으로 반환
        items_data = list(items.values('Brand', 'P_name', 'Price', 'Image', 'Longetivity', 'MBTI', 'Style', 'Skint_ype', 'Gender', 'Rate'))
        
        return JsonResponse({'items': items_data})

    return JsonResponse({'items': []})  # GET 요청이 아닌 경우 빈 응답

def get_items(request):
    brand = request.GET.get('brand')  # 쿼리 파라미터에서 'brand'를 가져옵니다.
    price_range = request.GET.get('price', '')  # 가격 필터 값
    page_number = request.GET.get('page', 1)
      # 기본적으로 모든 아이템을 가져옵니다.

    # 브랜드가 검색되었을 경우, 해당 브랜드로 필터링합니다.
    if brand:
        items = items.filter(Brand__icontains=brand)

    else:
        items = Item.objects.all()

    if price_range == 'below100':
        items = items.filter(Price__lt=100000)  # 여기서 items를 사용
    elif price_range == 'below200':
        items = items.filter(Q(Price__gte=100000) & Q(Price__lt=200000))  # 여기서 items를 사용
    elif price_range == 'above200':
        items = items.filter(Price__gte=200000)  # 여기서 items를 사용

    paginator = Paginator(items, 9)  # 페이지당 9개 아이템 표시
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': page_obj, 'brand': brand, 'price': price_range})


def mainpage(request):

    return render(request, 'index.html')