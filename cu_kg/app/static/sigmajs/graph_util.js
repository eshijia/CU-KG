var g, sigmaGraph;

function createGraphVisualization(data, div_name, relation_name) {
    if (data == null) {
        return;
    }

    var results = data.result;

    var nodeMap = {};
    g = {nodes: [], edges: []};

    var result, source, target, label;

    var source_color = "#ff8c00";   // dark orange
    var target_color = "#8b008b";   // dark magenta
    var edge_color = "#696969";     // dim gray
    var edge_hover_color = "#f00";  // red

    for (var i = 0; i < results.length; i++) {
        result = results[i];

        if (relation_name == null || (relation_name != null
            && result.predicate == relation_name)) {
            source = result.subject;
            target = result.object;

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
            edgeLabelSize: 'proportional',
            edgeHoverSizeRatio: 1,
            edgeHoverExtremities: true
        }
    });

    var dragListener = sigma.plugins.dragNodes(sigmaGraph, sigmaGraph.renderers[0]);
}


function createGraphVisualizationWithFlag(data, div_name) {
    if (data == null) {
        return;
    }

    var results = data.result;

    var nodeMap = {};
    g = {nodes: [], edges: []};

    var result, source, target, label, edge_color;

    var vertex_color = "#ff8c00";   // dark orange
    var xian_edge_color = "#9932cc";
    var ying_edge_color = "#335da8";
    var edge_hover_color = "#f00";   // red

    for (var i = 0; i < results.length; i++) {
        result = results[i];
        source = result.subject;
        target = result.object;

        if (nodeMap[source] !== true) {
            var data = {
                id: source,
                x: Math.random(),
                y: Math.random(),
                size: 10,
                color: vertex_color
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
                color: vertex_color
            };
            data.label = target;

            g.nodes.push(data);
            nodeMap[target] = true;
        }

        label = result.predicate;
        if (result.flag == 0) {
            edge_color = xian_edge_color;
        } else if (result.flag == 1) {
            edge_color = ying_edge_color;
        }

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
            edgeLabelSize: 'proportional',
            edgeHoverSizeRatio: 1,
            edgeHoverExtremities: true
        }
    });

    var dragListener = sigma.plugins.dragNodes(sigmaGraph, sigmaGraph.renderers[0]);
}