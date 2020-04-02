module.exports = {
    pathPrefix: "/COVID-19",
    siteMetadata: {
        title: `Visualizing COVID-19 Data`,
        description: `A page aiming to visualize the time aspects of the COVID-19 pandemy.`,
        author: `Felix Kratzer (@fez_de)`,
    },
    plugins: [
        `gatsby-plugin-react-helmet`,
        {
            resolve: `gatsby-source-filesystem`,
            options: {
                name: `images`,
                path: `${__dirname}/src/images`,
            },
        },
        `gatsby-plugin-sass`,
        `gatsby-transformer-sharp`,
        `gatsby-plugin-sharp`,
        {
            resolve: `gatsby-plugin-manifest`,
            options: {
                name: `gatsby-starter-react-bootstrap`,
                short_name: `react-bootstrap`,
                start_url: `/`,
                background_color: `#20232a`,
                theme_color: `#20232a`,
                display: `minimal-ui`,
            },
        },
        // this (optional) plugin enables Progressive Web App + Offline functionality
        // To learn more, visit: https://gatsby.dev/offline
        // `gatsby-plugin-offline`,
        {
            resolve: `gatsby-source-filesystem`,
            options: {
                // name: `docs images`,
                path: `${__dirname}/../docs-input`,

            },
        },
        {
            resolve: 'gatsby-source-filesystem',
            options: {
                name: `charts`,
                path: `${__dirname}/../charts/_current`,
            },
        },
        // `gatsby-transformer-remark`,
        {
            resolve: `gatsby-transformer-remark`,
            options: {
                plugins: [
                    {
                        resolve: `gatsby-remark-images`,
                        options: {
                            maxWidth: 1200,
                            linkImagesToOriginal: true,
                        },
                    },
                ],
            },
        },
        

    ],
}
