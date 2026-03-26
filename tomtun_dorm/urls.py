"""
URL configuration for tomtun_dorm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from management import views

# สร้างฟังก์ชันสำหรับเปิดหน้าแดชบอร์ดแบบง่ายๆ
def dashboard_view(request):
    return render(request, 'dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # หน้าแรก (Dashboard)
    path('rooms/', views.rooms, name='rooms'),    # <--- เพิ่มบรรทัดนี้: สำหรับหน้าจัดการห้องพัก
    path('contracts/', views.contracts, name='contracts'),  # <--- เพิ่มบรรทัดนี้
    path('check-in-out/', views.check_in_out, name='check_in_out'), # <--- เพิ่มบรรทัดนี้
]
