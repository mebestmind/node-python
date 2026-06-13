import { useState } from 'react'
import './App.css'

function App() {
  // 1. 상태(State) 만들기: 'name'이라는 공간에 이름을 저장하고, 기본값은 빈 칸('')으로 둡니다.
  const [name, setName] = useState('');

  // 2. 입력값이 바뀔 때마다 실행될 함수
  const handleInputChange = (event) => {
    // 사용자가 입력창에 타이핑한 값을 가져와서 name 상태를 업데이트합니다.
    setName(event.target.value);
  };

  return (
    <div className="card">
      <h2>👋 환영합니다!</h2>

      {/* 3. 입력창 생성 */}
      <input
        type="text"
        placeholder="이름을 입력해 주세요"
        value={name}
        onChange={handleInputChange}
        style={{ padding: '10px', fontSize: '16px', marginBottom: '20px' }}
      />

      {/* 4. 결과 출력: name 값이 있으면 메시지를 보여주고, 없으면 기본 메시지를 보여줍니다. */}
      <div>
        {name ? (
          <h3>안녕하세요, {name}님! 오늘 하루도 파이팅하세요! ✨</h3>
        ) : (
          <p>위에 이름을 입력하면 인사말이 나타납니다.</p>
        )}
      </div>
    </div>
  )
}

export default App