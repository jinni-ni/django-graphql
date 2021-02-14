from .types import RoomListResponse
from .models import Room

def resolve_rooms(root, info, page=1):
    print(info.context.user)
    if page < 1:
        page = 1
    page_size = 5
    skipping = (page - 1) * page_size
    taking = page_size * page
    rooms = Room.objects.all()[skipping:taking]
    total = Room.objects.count()
    return RoomListResponse(arr=rooms, total=total)


def resolve_room(root, info, id):
    # 사용자에게 doesnot exist 오류 보여줌
    return Room.objects.get(id=id)

