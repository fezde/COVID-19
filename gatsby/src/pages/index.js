import React from "react"
import { Row, Col, Container, Jumbotron } from "react-bootstrap"
import { graphql } from "gatsby"
import Post from "../components/Post"

import Layout from "../components/layout"
import SEO from "../components/seo"

const IndexPage = ({ data }) => (
    <Layout pageInfo={{ pageName: "index" }}>
        <SEO title="Home" keywords={[`gatsby`, `react`, `bootstrap`]} />
        <Container className="text-center">
            <Row>
                <Col>
                    <p>
                        This page tries to visualize the COVID-19 data provided by the Johns Hopkins University.
          </p>
                    <p>
                        While many pages visualize the current data on different levels, I have not yet seen any page that tries to focus on visualizing the timeline on a per-country level. This page shows the results of my visualizations.
          </p>
                    <Jumbotron>
                        <strong>Disclaimer</strong>: This page only is meant to display the data gathered by the Johns Hopkins University. I hereby disclaim any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability. Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited.
          </Jumbotron>
                </Col>
            </Row>
            {data.allMarkdownRemark.edges.map(({ node }, index) => {
                const parts = node.fileAbsolutePath.split("/");
                const fileName = parts[parts.length-1];
                console.log(fileName.split(".")[0]) ;  
                return (
                
                
                <Post
                    key={"POST_" + index}
                    image={fileName.split(".")[0]}
                    title={node.frontmatter.title}
                    content={node.html} />
                );
            }
                )
            }
        </Container>
    </Layout>
)

export default IndexPage

export const query = graphql`
  query {
    site {
        siteMetadata {
          title
        }
      }
      allMarkdownRemark(sort: { fields: [frontmatter___sorter], order: ASC }) {
        edges {
          node {
            html
            fileAbsolutePath
            frontmatter {
              title
             }
          }
        }
      }
  }
`