
import React from "react"
import { graphql } from "gatsby"
import Layout from "../components/layout"
import SEO from "../components/seo"

export default ({ data }) => {
    console.dir(data);
    const post = data.markdownRemark
    return (
        <Layout pageInfo={{ 
        pageName: data.markdownRemark.fields.slug,
        pageId: data.markdownRemark.id,
        }}>
            <SEO title={ post.frontmatter.title } />
            <div dangerouslySetInnerHTML={{ __html: post.html }} />
        </Layout>
    )
}

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      fields {
          slug
      }
      frontmatter {
        title
      }
      id
    }
  }
`