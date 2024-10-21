# search/management/commands/import_csv.py

import pandas as pd
from django.core.management.base import BaseCommand
from search.models import Item

class Command(BaseCommand):
    help = 'CSV 파일 데이터를 MySQL 데이터베이스에 업로드합니다.'

    def handle(self, *args, **kwargs):
        # CSV 파일 경로
        csv_file_path = '향수.csv'
        
        # pandas로 CSV 파일 읽기
        data = pd.read_csv(csv_file_path)
        
        # 데이터베이스에 저장
        for _, row in data.iterrows():

            Price = row['Price'].replace(',', '')  # 'Price' 컬럼에 대해 쉼표 제거
            Item.objects.get_or_create(
                Brand = row['Brand'],  # 항목 이름
                Price = Price,          # 가격
                Gender = row['Gender'],  # 성별
                P_name = row['향수이름(KOR)'], # 한글 향수 이름
                Name = row['Name'],  # 영어 향수 이름
                Rate = row['Rate'], # 평점
                Winter = row['Winter'],
                Spring = row['Spring'],
                Summer = row['Summer'],
                Fall =row['Fall'],
                season = row['season'],
                Day =row['Day'],
                Night = row['Night'],
                Main_Components = row['Main Components'],
                Top_Notes = row['Top Notes'],
                Middle_Notes = row['Middle Notes'],
                Base_Notes = row['Base Notes'],
                Longetivity = row['Longetivity'],
                Image = row['Image'],
                Skint_ype = row['Skin type'],
                Style = row['Style'],
                MBTI = row['MBTI'],
                description=row['설명글']
            )
        
        self.stdout.write(self.style.SUCCESS('CSV 파일 데이터를 MySQL 데이터베이스에 성공적으로 업로드했습니다.'))
