import React, { Component } from 'react';
import PostDetail from './PostDetail'

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
                  this.state.data.map((item, index) => {
                      return <PostDetail post={item} key={`post-list-key ${index}`}/>
                  })
                  :
              <h3>Wait for fetching</h3>
          }
      </div>
    );
  }
}

export default PostList;