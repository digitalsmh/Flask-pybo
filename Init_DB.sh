# 프로젝트  디렉토리로 이동
cd ~/projects/myproject

# 데이터베이스 파일, 디렉토리 삭제 
del pybo.db   
rm -rf migrations

# 데이터베이스 초기화   
flask db init    

# 리비전 파일 생성    
flask db migrate 

# 가장 최근 버전(리비전 파일 실행) DB upgrade   
flask db upgrade 

# 이전 버전으로 DB downgrade   
# flask db downgrade 