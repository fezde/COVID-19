import React, { Component } from "react"
import { StaticQuery, graphql } from "gatsby"
import {Row, Col, Image} from "react-bootstrap"


class Post extends Component {
    constructor(props) {
        super(props);

    }

    render_data = (data) => {
        const image = data.allFile.edges.find(
            edge => edge.node.name === this.props.image
        )
        console.log(data);
        console.log(image);
        return(
            
            <Row>
                <Col sm={8}>
                    <Image src={image.node.publicURL} fluid />
                </Col>
                <Col sm={4}>
                    <h3>{this.props.title}</h3>
                    <div dangerouslySetInnerHTML={{__html: this.props.content}}></div>
                </Col>
            </Row>
        );
    };

    render() {
        return (
            <StaticQuery
                query={graphql`
                query SiteTitleQueryFEZ {
                    allFile(filter: {ext: {eq: ".png"}, sourceInstanceName: {eq: "charts"}}) {
                        edges {
                          node {
                            publicURL
                            name
                          }
                        }
                      }
                }
                `}
                render={(data) => this.render_data(data)}
            />

        );
    }
}

export default Post;