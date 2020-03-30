import React, { Component } from "react"
import { Link } from "gatsby"
import { StaticQuery, graphql } from "gatsby"
import { Navbar, Nav } from "react-bootstrap"
import { node } from "prop-types";

// const CustomNavbar = ({ pageInfo }) => {
//     console.dir(pageInfo);
//     return (
//         <>
//             <Navbar variant="dark" expand="lg" id="site-navbar">
//                 {/* <Container> */}

//                 <Navbar.Toggle aria-controls="basic-navbar-nav" />
//                 <Navbar.Collapse id="basic-navbar-nav">
//                     <Link to="/" className="link-no-style">
//                         <Navbar.Brand as="span">Visualizations</Navbar.Brand>
//                     </Link>
//                     <Nav className="mr-auto" activeKey={pageInfo && pageInfo.pageName}>
//                         <Link to="/page-2" className="link-no-style">
//                             <Nav.Link as="span" eventKey="page-2">
//                                 Datasource and Copyright
//                             </Nav.Link>
//                         </Link>
//                     </Nav>

//                 </Navbar.Collapse>
//                 {/* </Container> */}
//             </Navbar>
//         </>
//     )
// }



class CustomNavbar extends Component {
    constructor(props) {
        super(props);
    }

    render_data = (data) => {

        return (
            data.allMarkdownRemark.edges.map((val) => {
                const node = val.node;
                console.dir(node);
                return (
                    <Link to={node.fields.slug} className="link-no-style" key={node.id}>
                        <Nav.Link as="span" eventKey={node.id}>
                            {node.frontmatter.title}
                        </Nav.Link>
                    </Link>
                );
            })

        );
    }
    render() {
        console.log(this.props);
        return (

            <Navbar variant="dark" expand="lg" id="site-navbar">
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Link to="/" className="link-no-style">
                        <Navbar.Brand as="span">Visualizations</Navbar.Brand>
                    </Link>
                    <Nav className="mr-auto" activeKey={this.props.pageInfo && this.props.pageInfo.pageId}>
                    {/* <Nav className="mr-auto" > */}
                        <StaticQuery
                            query={graphql`
                        query NavQueryFez {
                            allMarkdownRemark(filter: {frontmatter: {type: {eq: "page"}}}, sort: {fields: frontmatter___sorter, order: ASC}) {
                              edges {
                                node {
                                  fields {
                                    slug
                                  }
                                  id
                                  frontmatter {
                                    title
                                    sorter
                                    type
                                  }
                                }
                              }
                            }
                          }
                        `}
                            render={(data) => this.render_data(data)}
                        />
                    </Nav>
                </Navbar.Collapse>
            </Navbar>

        );
    }
}
export default CustomNavbar
