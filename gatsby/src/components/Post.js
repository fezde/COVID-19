import React, { Component } from "react"
import { StaticQuery, graphql } from "gatsby"
import { Row, Col, Image } from "react-bootstrap"
import { FaLink } from 'react-icons/fa';

class Post extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showOverlay: false,
        };
    }

    render_data = (data) => {
        const image_small = data.allFile.edges.find(
            edge => edge.node.name === this.props.image + "_small"
        );
        const image = data.allFile.edges.find(
            edge => edge.node.name === this.props.image
        );
        // console.log("render_data");
        // console.log(data); 
        // console.log(image);
        // console.log(image_small);

        const img = <Col sm={12} lg={8}>
            <a
                name={this.props.anchor}
                style={{ fontSize: "0.8em" }}
                onClick={(event) => { 
                    this.setState({ showOverlay: !this.state.showOverlay }); 

                    const scrollPosition = window.pageYOffset;
                    const offsetTop = document.getElementById(image_small.node.id).offsetTop;
                    console.log(scrollPosition);
                    console.log(offsetTop);
                    document.getElementById(image_small.node.id).scrollIntoView();
                    window.setTimeout(() => {
                        console.log("Plopp");
                        window.scroll(0, scrollPosition);
                    }, 100);
                }}
                href="#"
            >
                <Image 
                    src={image_small ? image_small.node.publicURL: "#"}
                    id = {image_small ? image_small.node.id: Math.random()}
                    fluid
                /><br />

                (Click to enlarge)
            </a>
        </Col>;

        let order = "order-sm-last";
        if (this.props.align === "left") {
            order = "order-sm-last order-lg-first";
        }

        const text = <Col sm={12} lg={4} className={order}>
            <h3 className="d-none d-lg-block">
                {this.props.title} &nbsp;
            <a href={ "#" + this.props.anchor}>
                <FaLink
                    color="#cccccc"
                    size="0.7em"
                />
            </a>
            </h3>

            <div
                style={{
                    textAlign: "left",
                }}
                dangerouslySetInnerHTML={{ __html: this.props.content }} />

        </Col>;



        return (
            <React.Fragment>
                <Row className="shadow-sm">
                    <div
                    id={this.props.anchor}
                    style={{
                        maxWidth: "0px",
                        maxHeight: "0px",
                        position: "relative",
                        top: "-70px",
                    }}>
                    </div>
                    <div style={{
                        background: "#000000af",
                        position: "fixed",
                        width: "100vw",
                        height: "100vh",
                        top: 0,
                        left: 0,
                        zIndex: 1000,
                        overscrollBehavior: "contain",
                        display: this.state.showOverlay ? "block" : "none"
                    }}
                        onClick={(event) => { 
                            this.setState({ showOverlay: !this.state.showOverlay }); 
                        }}
                    >
                        <Image src={image ? image.node.publicURL : "#"}
                            fluid
                            style={{
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
                    <Col style={{ minHeight: "40px" }}>&nbsp;</Col>
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
                        allFile(filter: {sourceInstanceName: {eq: "charts"}, publicURL: {}, ext: {regex: "/gif|png/"}}) {
                          edges {
                            node {
                              publicURL
                              name
                              id
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