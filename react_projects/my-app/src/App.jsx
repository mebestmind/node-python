import { useState, useEffect } from 'react';
import { supabase } from './supabaseClient';

function App() {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  // 수정(Update) 모드를 위한 상태 변수
  const [editingId, setEditingId] = useState(null);
  const [editTitle, setEditTitle] = useState('');
  const [editContent, setEditContent] = useState('');

  // 1. READ: 게시글 목록 불러오기 (최신순 정렬)
  const fetchPosts = async () => {
    const { data, error } = await supabase
      .from('posts')
      .select('*')
      .order('created_at', { ascending: false }); // 최신 글이 위로 오도록 설정

    if (error) console.error("데이터 불러오기 에러:", error);
    else setPosts(data);
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  // 2. CREATE: 새로운 게시글 등록
  const addPost = async (e) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) {
      alert("제목과 내용을 모두 입력해주세요.");
      return;
    }

    const { error } = await supabase
      .from('posts')
      .insert([{ title, content }]); // id와 created_at은 자동으로 생성됨

    if (error) console.error("게시글 등록 에러:", error);
    else {
      setTitle('');
      setContent('');
      fetchPosts(); // 목록 갱신
    }
  };

  // 3. UPDATE: 게시글 수정 처리
  const updatePost = async (e) => {
    e.preventDefault();
    if (!editTitle.trim() || !editContent.trim()) {
      alert("수정할 제목과 내용을 입력해주세요.");
      return;
    }

    const { error } = await supabase
      .from('posts')
      .update({ title: editTitle, content: editContent })
      .eq('id', editingId);

    if (error) console.error("게시글 수정 에러:", error);
    else {
      setEditingId(null); // 수정 모드 종료
      fetchPosts(); // 목록 갱신
    }
  };

  // 수정 모드 활성화 (기존 데이터를 수정창에 채워넣음)
  const startEdit = (post) => {
    setEditingId(post.id);
    setEditTitle(post.title);
    setEditContent(post.content);
  };

  // 4. DELETE: 게시글 삭제
  const deletePost = async (id) => {
    if (!window.confirm("정말 이 게시글을 삭제하시겠습니까?")) return;

    const { error } = await supabase
      .from('posts')
      .delete()
      .eq('id', id);

    if (error) console.error("게시글 삭제 에러:", error);
    else fetchPosts();
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Supabase 게시판 CRUD</h1>

      {/* --- 작성 및 수정 폼 영역 --- */}
      {editingId ? (
        // 수정 중일 때 보여지는 폼
        <form onSubmit={updatePost} style={{ marginBottom: '30px', padding: '15px', border: '2px solid #007bff', borderRadius: '5px' }}>
          <h3>게시글 수정하기</h3>
          <input
            type="text"
            value={editTitle}
            onChange={(e) => setEditTitle(e.target.value)}
            placeholder="수정할 제목"
            style={{ width: '100%', padding: '10px', marginBottom: '10px', boxSizing: 'border-box' }}
          />
          <textarea
            value={editContent}
            onChange={(e) => setEditContent(e.target.value)}
            placeholder="수정할 내용"
            rows="4"
            style={{ width: '100%', padding: '10px', marginBottom: '10px', boxSizing: 'border-box' }}
          />
          <button type="submit" style={{ padding: '10px 15px', backgroundColor: '#007bff', color: 'white', border: 'none', cursor: 'pointer', marginRight: '5px' }}>수정 완료</button>
          <button type="button" onClick={() => setEditingId(null)} style={{ padding: '10px 15px', backgroundColor: '#6c757d', color: 'white', border: 'none', cursor: 'pointer' }}>취소</button>
        </form>
      ) : (
        // 기본 작성 폼
        <form onSubmit={addPost} style={{ marginBottom: '30px', padding: '15px', border: '1px solid #ccc', borderRadius: '5px' }}>
          <h3>새 게시글 작성</h3>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="제목을 입력하세요"
            style={{ width: '100%', padding: '10px', marginBottom: '10px', boxSizing: 'border-box' }}
          />
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder="내용을 입력하세요"
            rows="4"
            style={{ width: '100%', padding: '10px', marginBottom: '10px', boxSizing: 'border-box' }}
          />
          <button type="submit" style={{ padding: '10px 20px', backgroundColor: '#28a745', color: 'white', border: 'none', cursor: 'pointer' }}>등록</button>
        </form>
      )}

      {/* --- 게시글 목록 출력 영역 --- */}
      <div>
        <h3>게시글 목록 ({posts.length})</h3>
        {posts.length === 0 ? (
          <p>등록된 게시글이 없습니다.</p>
        ) : (
          posts.map((post) => (
            <div key={post.id} style={{ padding: '15px', border: '1px solid #ddd', borderRadius: '5px', marginBottom: '15px', backgroundColor: '#f9f9f9' }}>
              <h4 style={{ margin: '0 0 10px 0', color: '#333' }}>{post.title}</h4>
              <p style={{ margin: '0 0 15px 0', color: '#666', whiteSpace: 'pre-wrap' }}>{post.content}</p>
              <small style={{ color: '#999' }}>작성일: {new Date(post.created_at).toLocaleString()}</small>

              <div style={{ marginTop: '10px', textAlign: 'right' }}>
                <button onClick={() => startEdit(post)} style={{ padding: '5px 10px', marginRight: '5px', backgroundColor: '#ffc107', border: 'none', cursor: 'pointer' }}>수정</button>
                <button onClick={() => deletePost(post.id)} style={{ padding: '5px 10px', backgroundColor: '#dc3545', color: 'white', border: 'none', cursor: 'pointer' }}>삭제</button>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;