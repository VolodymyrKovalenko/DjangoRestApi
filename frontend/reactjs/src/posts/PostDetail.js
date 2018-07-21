import React, { Component } from 'react';
import { Button, Container,Row,Col } from 'reactstrap';

class PostDetail extends Component {
    constructor(props){
        super(props);
        this.toggleContent = this.toggleContent.bind(this);
        this.state = {
            showContent : false
        }
    }
    toggleContent(event){
        event.preventDefault();
        this.setState({
            showContent: !this.state.showContent
        })
    }

  render() {
    const {post} = this.props;
    // const {showContent} = this.state;
    return   (
        <Container>
            <Row>
            <Col sm="12" md={{ size: 6, offset: 3 }}>
              <div>
                <h3>{post.title}</h3>
                  {this.state.showContent === true ?
                      <div>
                          <div>{post.content}</div>
                          <Button color="info" size="sm" onClick={this.toggleContent}>Hide content</Button>
                      </div>:
                      <Button color="info" outline size="sm" onClick={this.toggleContent}>Show content</Button>
                  }
                <p>Author: <b>{post.author.username}</b></p>

              </div>
            </Col>
            </Row>
        </Container>
    );
  }
}

export default PostDetail;