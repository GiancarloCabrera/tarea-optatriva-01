import clips

workspace = clips.Environment()

workspace.build('(deftemplate user (slot likes) (slot travel_style) (slot budget))')
workspace.build('(deftemplate suggestion (slot destination))')

workspace.build('''
(defrule adventure-low-budget-group
    (user (likes adventure) (travel_style group) (budget low))
    =>
    (assert (suggestion (destination "Mountain hiking trip"))))
''')

workspace.build('''
(defrule adventure-medium-budget-group
    (user (likes adventure) (travel_style group) (budget medium))
    =>
    (assert (suggestion (destination "La Vaca Cave"))))
''')

workspace.build('''
(defrule adventure-high-budget-group
    (user (likes adventure) (travel_style group) (budget high))
    =>
    (assert (suggestion (destination "Trip to Greenland"))))
''')

workspace.build('''
(defrule adventure-high-budget-solo
    (user (likes adventure) (travel_style solo) (budget high))
    =>
    (assert (suggestion (destination "Trip to Egypt"))))
''')

workspace.build('''
(defrule adventure-medium-budget-solo
    (user (likes adventure) (travel_style solo) (budget medium))
    =>
    (assert (suggestion (destination "Safari in Africa"))))
''')

workspace.build('''
(defrule adventure-low-budget-solo
    (user (likes adventure) (travel_style solo) (budget low))
    =>
    (assert (suggestion (destination "Skydiving"))))
''')

workspace.build('''
(defrule adventure-high-budget-family
    (user (likes adventure) (travel_style family) (budget high))
    =>
    (assert (suggestion (destination "Disney World"))))
''')

workspace.build('''
(defrule adventure-medium-budget-family
    (user (likes adventure) (travel_style family) (budget medium))
    =>
    (assert (suggestion (destination "Tatacoa Desert"))))
''')

workspace.build('''
(defrule adventure-low-budget-family
    (user (likes adventure) (travel_style family) (budget low))
    =>
    (assert (suggestion (destination "Comfama Arvi Park"))))
''')

workspace.build('''
(defrule beach-high-budget-family
    (user (likes beach) (travel_style family) (budget high))
    =>
    (assert (suggestion (destination "Luxury resort in the Caribbean"))))
''')

workspace.build('''
(defrule beach-medium-budget-family
    (user (likes beach) (travel_style family) (budget medium))
    =>
    (assert (suggestion (destination "Decameron Cartagena"))))
''')

workspace.build('''
(defrule beach-low-budget-family
    (user (likes beach) (travel_style family) (budget low))
    =>
    (assert (suggestion (destination "Hotel two blocks from the beach"))))
''')


workspace.build('''
(defrule nature-low-budget
    (user (likes nature) (travel_style family) (budget low))
    =>
    (assert (suggestion (destination "Camping in a national park"))))
''')

workspace.build('''
(defrule culture-medium-budget
    (user (likes culture) (travel_style group) (budget medium))
    =>
    (assert (suggestion (destination "Visit to temples in Japan"))))
''')

workspace.build('''
(defrule city-low-budget-solo
    (user (likes city) (travel_style solo) (budget low))
    =>
    (assert (suggestion (destination "Backpacking in Eastern Europe"))))
''')

workspace.build('''
(defrule city-medium-budget-solo
    (user (likes city) (travel_style solo) (budget medium))
    =>
    (assert (suggestion (destination "Cultural tour in Paris"))))
''')

workspace.build('''
(defrule city-high-budget-solo
    (user (likes city) (travel_style solo) (budget high))
    =>
    (assert (suggestion (destination "Luxury trip to New York City"))))
''')

workspace.build('''
(defrule city-low-budget-group
    (user (likes city) (travel_style group) (budget low))
    =>
    (assert (suggestion (destination "City break in Southeast Asia"))))
''')

workspace.build('''
(defrule city-medium-budget-group
    (user (likes city) (travel_style group) (budget medium))
    =>
    (assert (suggestion (destination "Weekend in Rome"))))
''')

workspace.build('''
(defrule city-high-budget-group
    (user (likes city) (travel_style group) (budget high))
    =>
    (assert (suggestion (destination "Gourmet trip to Tokyo"))))
''')

workspace.build('''
(defrule city-low-budget-family
    (user (likes city) (travel_style family) (budget low))
    =>
    (assert (suggestion (destination "Staycation in a nearby city"))))
''')

workspace.build('''
(defrule city-medium-budget-family
    (user (likes city) (travel_style family) (budget medium))
    =>
    (assert (suggestion (destination "Family trip to Madrid"))))
''')

workspace.build('''
(defrule city-high-budget-family
    (user (likes city) (travel_style family) (budget high))
    =>
    (assert (suggestion (destination "Exploration of Dubai"))))
''')

def generate_suggestion(likes=None, travel_style=None, budget=None):
    workspace.reset()

    if likes and travel_style and budget:
        workspace.assert_string(f'(user (likes {likes}) (travel_style {travel_style}) (budget {budget}))')

    workspace.run()

    suggestions = []
    for fact in workspace.facts():
        if fact.template.name == 'suggestion':
            suggestions.append(fact['destination'])

    return suggestions
