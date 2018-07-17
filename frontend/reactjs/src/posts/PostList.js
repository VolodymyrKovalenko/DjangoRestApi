import React, { Component } from 'react';

class PostList extends Component {
    constructor(){
        super();
        this.state ={
            data:null,
        };
        this.getData();
    }
    getData(){
        fetch('http://127.0.0.1:8000/posts/').then((resp)=>{
            resp.json().then((res)=>{
                this.setState({data:res})
            })
        })
    }
  render() {
    return (
      <div>
          {
              this.state.data ?
                  this.state.data.map((item) =>
                      <div>
                        <h3>{item.title}</h3>
                        <div>{item.content}</div>
                          <h5>{item.author.username}</h5>
                      </div>
                  )
                  :
              <h3>Wait for fetching</h3>
          }
      </div>
    );
  }
}

export default PostList;