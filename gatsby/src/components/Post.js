import React, { Component } from "react"
import { StaticQuery, graphql } from "gatsby"
import {Row, Col, Image } from "react-bootstrap"


class Post extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showOverlay: false, 
        };
    }

    render_data = (data) => {
        const image_small = data.allFile.edges.find(
            edge => edge.node.name === this.props.image+"_small"
        );
        const image = data.allFile.edges.find(
            edge => edge.node.name === this.props.image
        );
        console.log(data);
        console.log(image);

        const img = <Col sm={12} lg={8}>
            <a 
            name={this.props.anchor}
            style={{fontSize: "0.8em"}}
            onClick={(event) => { this.setState({showOverlay: !this.state.showOverlay }); }}
            href="#"
            >
                <Image src={image_small.node.publicURL} 
                    fluid  
                /><br/>
            
                (Click to enlarge)
            </a>
        </Col>;

        let order = "order-sm-last";
        if(this.props.align === "left"){
            order = "order-sm-last order-lg-first";
        }

        const text = <Col sm={12} lg={4} className={order}>
            <h3 className="d-none d-lg-block">
            {this.props.title}
             - {this.props.align}
            </h3>

            <div 
                style={{
                    textAlign: "left",
                }}
                dangerouslySetInnerHTML={{ __html: this.props.content }} />

        </Col>;

    

        return(
            <React.Fragment>
                <Row id={this.props.anchor} className="shadow-sm">
                    <div style={{
                        background: "#000000af",
                        position: "fixed",
                        width: "100vw",
                        height: "100vh",
                        top: 0,
                        left: 0,
                        zIndex: 1000,
                        display: this.state.showOverlay ? "block": "none"  
                    }}
                    onClick={(event) => { this.setState({showOverlay: !this.state.showOverlay }); }}
                    >
                        <Image src={image.node.publicURL}
                            fluid  
                            style = {{
                                maxWidth: "90vw",
                                maxHeight: "95vh",
                                position: "absolute",
                                left: "50vw",
                                top: "50vh",
                                transform: "translate(-50%, -50%)"
                            }}
                            />
                    </div>
                    <Col sm={12} className="d-block d-lg-none">
                        <h3>{this.props.title}</h3>
                    </Col>
                    {img}{text}
                    
                </Row>
                <Row>
                    <Col style={{minHeight: "40px"}}>&nbsp;</Col>
                </Row>
            </React.Fragment>
        );
    };

    render() {
        return (
            <React.Fragment>
                
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
            </React.Fragment>
            

        );
    }
}

export default Post;