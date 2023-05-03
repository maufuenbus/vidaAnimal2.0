import React from 'react';

function Card() {
  return (
    <div className='container'>
      <div className="card" style={{ width: '18rem' }}>
        <img src="https://mdbcdn.b-cdn.net/img/new/standard/city/062.webp" className="card-img-top" alt="Chicago Skyscrapers" />
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
        
      </div>
      <div className="card" style={{ width: '18rem' }}>
      <img src="https://mdbcdn.b-cdn.net/img/new/standard/city/062.webp" className="card-img-top" alt="Chicago Skyscrapers" />
      <div className="card-body">
        <h5 className="card-title">Card title</h5>
        <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      </div>
      
    </div>
      <div className="card" style={{ width: '18rem' }}>
      <img src="https://mdbcdn.b-cdn.net/img/new/standard/city/062.webp" className="card-img-top" alt="Chicago Skyscrapers" />
      <div className="card-body">
        <h5 className="card-title">Card title</h5>
        <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      </div>
      
    </div>
  </div>
  );
}

export default Card;
