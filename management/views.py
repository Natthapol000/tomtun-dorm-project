from django.shortcuts import render
from .models import Room

def dashboard(request):
    # --- ข้อมูลจริงจากฐานข้อมูล (คอมเมนต์ไว้ก่อนชั่วคราว) ---
    # total_rooms = Room.objects.count() 
    # available_rooms = Room.objects.filter(status='available').count() 
    # occupied_rooms = Room.objects.filter(status='occupied').count() 
    # maintenance_rooms = Room.objects.filter(status='maintenance').count() 

    # --- ข้อมูลจำลอง (Mock Data) อิงตาม Figma เอามาจัด UI ---
    context = {
        'total_rooms': 120,            # เปลี่ยนเป็น 120 ห้อง
        'available_rooms': 20,         # ว่าง 20
        'occupied_rooms': 95,          # มีผู้เช่า 95
        'maintenance_rooms': 5,        # ซ่อม 5
        'revenue': "540,000",          # รายได้
        'overdue': "15,000",           # ค้างชำระ
        'growth_percentage': 85        # อัตราการเข้าพัก
    }
    
    return render(request, 'dashboard.html', context)
def rooms(request):
    # อนาคตเราจะดึงข้อมูลห้องจากฐานข้อมูลตรงนี้ 
    # แต่ตอนนี้ให้ render หน้า HTML เปล่าๆ ไปจัด UI ก่อน
    return render(request, 'rooms.html')
def contracts(request):
    return render(request, 'contracts.html')
def check_in_out(request):
    return render(request, 'check_in_out.html')