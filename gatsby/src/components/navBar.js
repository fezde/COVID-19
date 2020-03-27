import React from "react"
import { Link } from "gatsby"

import { Navbar, Nav } from "react-bootstrap"

const CustomNavbar = ({ pageInfo }) => {
    return (
        <>
            <Navbar variant="dark" expand="lg" id="site-navbar">
                {/* <Container> */}
                
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Link to="/" className="link-no-style">
                        <Navbar.Brand as="span">Visualizations</Navbar.Brand>
                    </Link>
                    <Nav className="mr-auto" activeKey={pageInfo && pageInfo.pageName}>
                        <Link to="/page-2" className="link-no-style">
                            <Nav.Link as="span" eventKey="page-2">
                                Datasource and Copyright
              </Nav.Link>
                        </Link>
                    </Nav>

                </Navbar.Collapse>
                {/* </Container> */}
            </Navbar>
        </>
    )
}

export default CustomNavbar
