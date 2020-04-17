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

        {
            resolve: `gatsby-plugin-goatcounter`,
            options: {
                // REQUIRED! https://[my_code].goatcounter.com
                code: 'visualizingcovid19',

                // ALL following settings are OPTIONAL

                // Avoids sending pageview hits from custom paths
                //exclude: [],

                // Delays sending pageview hits on route update (in milliseconds)
                pageTransitionDelay: 0,

                // Defines where to place the tracking script
                // boolean `true` in the head and `false` in the body
                head: false,

                // Set to true to include a gif to count non-JS users
                pixel: false,

                // Allow requests from local addresses (localhost, 192.168.0.0, etc.)
                // for testing the integration locally.
                // TIP: set up a `Additional Site` in your GoatCounter settings
                // and use its code conditionally when you `allowLocal`, example below
                allowLocal: false,

                // Override the default localStorage key more below
                localStorageKey: 'skipgc',

                // Set to boolean true to enable referrer set via URL parameters
                // Like example.com?ref=referrer.com or example.com?utm_source=referrer.com
                // Accepts a function to override the default referrer extraction
                // NOTE: No Babel! The function will be passes as is to your websites <head> section
                // So make sure the function works as intended in all browsers you want to support
                referrer: true,

                // Setting it to boolean true will clean the URL from
                // `?ref` & `?utm_` parameters before sending it to GoatCounter
                // It uses `window.history.replaceState` to clean the URL in the
                // browser address bar as well.
                // This is to prevent ref tracking ending up in your users bookmarks.
                // All parameters other than `ref` and all `utm_` will stay intact
                urlCleanup: false,
            },
        },

    ],
}
