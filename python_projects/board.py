import os
from supabase import create_client, Client

# 1. Supabase 연동 설정 (실제 환경에서는 환경변수(os.environ) 사용을 권장합니다)
SUPABASE_URL = "https://fjapwqhezsuyuwohgjvg.supabase.co"
SUPABASE_KEY = "sb_publishable_PEdqniopHZSJh65jLnLbMQ_Yo2gDzUs"   # Publishable key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# 2. 게시글 작성 (Create)
def create_post(title: str, content: str):
    data, count = supabase.table("posts").insert({"title": title, "content": content}).execute()
    print(f"[성공] 게시글이 작성되었습니다: {data[1][0]['title']}")


# 3. 게시글 목록 조회 (Read)
def get_posts():
    data, count = supabase.table("posts").select("*").order("created_at", desc=True).execute()
    print("\n--- 게시글 목록 ---")
    for post in data[1]:
        print(f"[{post['id']}] {post['title']} | 작성일: {post['created_at'][:10]}")
    print("-------------------\n")


# 4. 게시글 수정 (Update)
def update_post(post_id: int, new_title: str, new_content: str):
    data, count = supabase.table("posts").update({"title": new_title, "content": new_content}).eq("id",
                                                                                                  post_id).execute()
    if data[1]:
        print(f"[성공] {post_id}번 게시글이 수정되었습니다.")
    else:
        print("[실패] 해당 게시글을 찾을 수 없습니다.")


# 5. 게시글 삭제 (Delete)
def delete_post(post_id: int):
    data, count = supabase.table("posts").delete().eq("id", post_id).execute()
    if data[1]:
        print(f"[성공] {post_id}번 게시글이 삭제되었습니다.")
    else:
        print("[실패] 해당 게시글을 찾을 수 없습니다.")


# --- 실행 테스트 ---
if __name__ == "__main__":
    # 테스트용 데이터 생성
    create_post("첫 번째 글", "Supabase와 파이썬 연동 테스트입니다.")
    create_post("두 번째 글", "게시판 만들기 정말 쉽네요!")

    # 목록 조회
    get_posts()

    # 1번 글 수정 (1번 글이 존재한다고 가정)
    update_post(3, "수정된 첫 번째 글 제목", "내용도 이렇게 수정할 수 있습니다.")

    # 다시 목록 조회
    get_posts()

    # 2번 글 삭제
    delete_post(4)

    # 최종 목록 조회
    get_posts()