var g, sigmaGraph;

function createGraphVisualization(data, div_name, relation_name) {

    var results = data.result;

    var nodeMap = {};
    g = {nodes:[], edges: []};

    var result, source, target, label;

    for (var i = 0; i < results.length; i++) {
        result = results[i];

        if (relation_name == null || (relation_name != null
            && result.predicate == relation_name)) {
            source = result.subject;
            target = result.object;

            source_color = "#ff8c00";   // dark orange
            target_color = "#8b008b";   // dark magenta
            edge_color = "#696969";     // dim gray
            edge_hover_color = "#f00";  // red

            if (nodeMap[source] !== true) {
                var data = {
                    id: source,
                    x: Math.random(),
                    y: Math.random(),
                    size: 10,
                    color: source_color
                };
                data.label = source;

                g.nodes.push(data);
                nodeMap[source] = true;
            }

            if (nodeMap[target] !== true) {
                var data = {
                    id: target,
                    x: Math.random(),
                    y: Math.random(),
                    size: 10,
                    color: target_color
                };
                data.label = target;

                g.nodes.push(data);
                nodeMap[target] = true;
            }

            label = result.predicate;
            g.edges.push({
               id: "e" + i,
                label: label,
                source: source,
                target: target,
                size: 3,
                color: edge_color,
                hover_color: edge_hover_color,
                type: "curvedArrow"
            });
        }
    }

    sigma.renderers.def = sigma.renderers.canvas;
    sigmaGraph = new sigma({
        graph: g,
        container: div_name,
        settings: {
            doubleClickEnabled: false,
            minEdgeSize: 0.5,
            maxEdgeSize: 4,
            enableEdgeHovering: true,
            edgeHoverColor: 'edge',
            defaultNodeColor: '#ec5148',
            edgeLabelSize: 'proportional',
            defaultEdgeHoverColor: '#000',
            edgeHoverSizeRatio: 1,
            edgeHoverExtremities: true
        }
    });

    var dragListener = sigma.plugins.dragNodes(sigmaGraph, sigmaGraph.renderers[0]);
}