import cPickle, base64
try:
	from SimpleSession.versions.v54 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 6, 1, 35849])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v54 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwBOfYdVCWJhbGxTY2FsZXEDSwBOfYdVCXBvaW50U2l6ZXEESwBOfYdVBWNvbG9ycQVLAE59h1UKcmliYm9uVHlwZXEGSwBOfYdVCnN0aWNrU2NhbGVxB0sATn2HVQxhcm9tYXRpY01vZGVxCEsATn2HVQp2ZHdEZW5zaXR5cQlLAE59h1UGaGlkZGVucQpLAE59h1UNYXJvbWF0aWNDb2xvcnELSwBOfYdVD3JpYmJvblNtb290aGluZ3EMSwBOfYdVCWF1dG9jaGFpbnENSwBOfYdVCG9wdGlvbmFscQ59VQ9sb3dlckNhc2VDaGFpbnNxD0sATn2HVQlsaW5lV2lkdGhxEEsATn2HVQ9yZXNpZHVlTGFiZWxQb3NxEUsATn2HVQRuYW1lcRJLAE59h1UPYXJvbWF0aWNEaXNwbGF5cRNLAE59h1UPcmliYm9uU3RpZmZuZXNzcRRLAE59h1UKcGRiSGVhZGVyc3EVXVUDaWRzcRZLAE59h1UOc3VyZmFjZU9wYWNpdHlxF0sATn2HVRBhcm9tYXRpY0xpbmVUeXBlcRhLAE59h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xGUsATn2HVQdkaXNwbGF5cRpLAE59h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksATn2HVQtmaWxsRGlzcGxheXEDSwBOfYdVBG5hbWVxBEsATn2HVQVjaGFpbnEFSwBOfYdVDnJpYmJvbkRyYXdNb2RlcQZLAE59h1UCc3NxB0sATn2HVQhtb2xlY3VsZXEISwBOfYdVC3JpYmJvbkNvbG9ycQlLAE59h1UFbGFiZWxxCksATn2HVQpsYWJlbENvbG9ycQtLAE59h1UIZmlsbE1vZGVxDEsATn2HVQVpc0hldHENSwBOfYdVC2xhYmVsT2Zmc2V0cQ5LAE59h1UIcG9zaXRpb25xD11VDXJpYmJvbkRpc3BsYXlxEEsATn2HVQhvcHRpb25hbHERfVUEc3NJZHESSwBOfYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLAE59h1UIdmR3Q29sb3JxA0sATn2HVQRuYW1lcQRLAE59h1UDdmR3cQVLAE59h1UOc3VyZmFjZURpc3BsYXlxBksATn2HVQVjb2xvcnEHSwBOfYdVCWlkYXRtVHlwZXEISwBOfYdVBmFsdExvY3EJSwBOfYdVBWxhYmVscQpLAE59h1UOc3VyZmFjZU9wYWNpdHlxC0sATn2HVQdlbGVtZW50cQxLAE59h1UKbGFiZWxDb2xvcnENSwBOfYdVDHN1cmZhY2VDb2xvcnEOSwBOfYdVD3N1cmZhY2VDYXRlZ29yeXEPSwBOfYdVBnJhZGl1c3EQSwBOfYdVC2xhYmVsT2Zmc2V0cRFLAE59h1USbWluaW11bUxhYmVsUmFkaXVzcRJLAE59h1UIZHJhd01vZGVxE0sATn2HVQhvcHRpb25hbHEUfVUHZGlzcGxheXEVSwBOfYd1Lg=='))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXVUFbGFiZWxxA0sATn2HVQZyYWRpdXNxBEsATn2HVQtsYWJlbE9mZnNldHEFSwBOfYdVCGRyYXdNb2RlcQZLAE59h1UIb3B0aW9uYWxxB31VB2Rpc3BsYXlxCEsATn2HdS4='))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQEu'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'gold': ((1, 0.843137, 0), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'orange': ((1, 0.498039, 0), 1, u'default'), '_openColor00': ((1, 1, 1), 1, u'default'), '_openColor01': ((1, 0, 1), 1, u'default'), '_openColor02': ((0, 1, 1), 1, u'default'), '_openColor03': ((1, 1, 0), 1, u'default'), '_openColor04': ((1, 0, 0), 1, u'default'), '_openColor05': ((0, 0, 1), 1, u'default'), '_openColor06': ((0.67, 1, 0), 1, u'default'),
'_openColor07': ((0.67, 0, 1), 1, u'default'), '_openColor08': ((0.67, 1, 1), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'orange red': ((1, 0.270588, 0), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'), '_openColor12': ((1, 1, 0.5), 1, u'default'), '_openColor11': ((1, 0.67, 1), 1, u'default'), '_openColor10': ((0, 0.67, 1), 1, u'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'),
'purple': ((0.627451, 0.12549, 0.941176), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'khaki': ((0.941176, 0.901961, 0.54902), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'sky blue': ((0.529412, 0.807843, 0.921569), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), 'plum': ((0.866667, 0.627451, 0.866667), 1, u'default'), 'hot pink': ((1, 0.411765, 0.705882), 1, u'default'), 'Eu': ((0.380392, 1, 0.780392), 1, u'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'),
'Er': ((0, 0.901961, 0.458824), 1, u'default'), '_openColor13': ((1, 0, 0.5), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), '_openColor15': ((0.67, 0.67, 1), 1, u'default'), '_openColor14': ((0, 1, 0.5), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'),
'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'coral': ((1, 0.498039, 0.313725), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'brown': ((0.647059, 0.164706, 0.164706), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'),
'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), 'light blue': ((0.678431, 0.847059, 0.901961), 1, u'default'), 'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'pink': ((1, 0.752941, 0.796078), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'navy blue': ((0, 0, 0.501961), 1, u'default'), '_openColor09': ((1, 0.67, 0), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'salmon': ((0.980392, 0.501961, 0.447059), 1, u'default'), 'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'),
'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), 'dark green': ((0, 0.392157, 0), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor', u'missing segments'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}, {'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (2, 2, {}), 'color': (2, 0, {1: [1]}), 'optional': {'fixedLabels': (True, False, (2, False, {None: [1]}))}, 'display': (2, True, {}), 'showStubBonds': (2, False, {}), 'lineWidth': (2, 1, {}), 'stickScale': (2, 1, {}), 'id': [-2, -1]}
	modelAssociations = {}
	colorInfo = (5, (u'black', (0, 0, 0, 1)), {(u'green', (0, 1, 0, 1)): [4], (u'', (1, 1, 1, 1)): [3], (u'yellow', (1, 1, 0, 1)): [0], (u'gray', (0.745, 0.745, 0.745, 1)): [1]})
	viewerInfo = {'cameraAttrs': {'center': (1594.79, -469.465, 385.529), 'fieldOfView': 25, 'nearFar': (1320.62, -549.567), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 1004.37}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'viewSize': 2473.25, 'labelsOnTop': True, 'depthCueRange': (0.5, 1.05556), 'silhouetteWidth': 1, 'singleLayerTransparency': True, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 3.15765, 'backgroundMethod': 0}, 'viewerHL': 4, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': 2, 'viewerBG': 3}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v54 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


def restore_surface_color_mapping():
 try:
  surface_color_state = \
   {
    'class': 'Surface_Colorings_State',
    'coloring_table': {},
    'geometry': None,
    'is_visible': False,
    'version': 2,
   }
  import SurfaceColor.session
  SurfaceColor.session.restore_surface_color_state(surface_color_state)
 except:
  reportRestoreError('Error restoring surface color mapping')

registerAfterModelsCB(restore_surface_color_mapping)


def restore_hide_dust():
 hide_dust_state = \
   {
    'class': 'Hide_Dust_State',
    'dust_table': {},
    'version': 1,
   }
 try:
  import HideDust.session
  HideDust.session.restore_hide_dust_state(hide_dust_state)
 except:
  reportRestoreError('Error restoring hide dust')

registerAfterModelsCB(restore_hide_dust)


def restore_color_zones():
 color_zone_state = \
   {
    'class': 'Color_Zone_State',
    'color_zone_table': {},
    'version': 2,
   }
 try:
  import ColorZone.session
  ColorZone.session.restore_color_zone_state(color_zone_state)
 except:
  reportRestoreError('Error restoring surface color zones')

registerAfterModelsCB(restore_color_zones)


def restore_surface_zones():
 surface_zone_state = \
   {
    'class': 'Surface_Zone_State',
    'version': 3,
    'zone_table': {},
   }
 try:
  import SurfaceZone.session
  SurfaceZone.session.restore_surface_zone_state(surface_zone_state)
 except:
  reportRestoreError('Error restoring surface zones')

registerAfterModelsCB(restore_surface_zones)


def restore_multiscale():
 multiscale_state = \
  {
   'class': 'Multiscale_Dialog_State',
   'density_threshold': '0.02',
   'density_threshold_ca_only': '0.002',
   'geometry': '403x492+625+72',
   'is_visible': False,
   'lan_molecule_states': [ ],
   'model_states': [ ],
   'multimer_type': 'Biological unit',
   'rgba': ( 0.9629629629629629, 0.5555555555555556, 0.18518518518518517, 1, ),
   'smoothing_factor': '0.3',
   'smoothing_iterations': '2',
   'surface_resolution': '3',
   'transparency': '0',
   'version': 3,
  }
 import MultiScale.session
 MultiScale.session.restore_multiscale_state(multiscale_state)

try:
  restore_multiscale()
except:
  reportRestoreError('Error restoring multiscale')


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'hiv_debris.mrc',
       'path': 'hiv_debris.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 92, 90, 100, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 92, 90, 100, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': True,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'outline_box_linewidth': 1,
          'outline_box_rgb': ( 1, 1, 1, ),
          'projection_mode': '2d-xyz',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': True,
          'two_sided_lighting': False,
          'version': 1,
          'voxel_limit': 1,
         },
        'representation': 'surface',
        'session_volume_id': u'hiv_debris.mrc',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
         ],
        'solid_levels': [
          ( 128.30809143066406, 0, ),
          ( 133.8867041015625, 0.5, ),
          ( 139.46531677246094, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.9333333333333333, 0.7333333333333333, 0.2, 1.0, ),
         ],
        'surface_levels': [ 128.30809143066406, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( -0.7682877548203362, -0.28954374707755276, 0.570875068926133, ),
          'clip_plane_origin': ( 906.2431945800781, 696.9441375732422, 2264.2266235351562, ),
          'clip_thickness': 101.87811279296875,
          'display': True,
          'id': 13,
          'name': u'hiv_debris.mrc',
          'osl_identifier': u'#13',
          'subid': 0,
          'use_clip_plane': True,
          'use_clip_thickness': False,
          'version': 4,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 121.23087465179997,
            'rotation_axis': ( -0.06788996622211037, -0.9824555167687113, 0.17370120914111448, ),
            'translation': ( 4056.118390608411, -783.5125895730275, 970.1068364749497, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.010989010457460207,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'hiv_envelope.mrc',
       'path': 'hiv_envelope.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 92, 90, 100, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 92, 90, 100, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': True,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'outline_box_linewidth': 1,
          'outline_box_rgb': ( 1, 1, 1, ),
          'projection_mode': '2d-xyz',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': True,
          'two_sided_lighting': False,
          'version': 1,
          'voxel_limit': 1,
         },
        'representation': 'surface',
        'session_volume_id': u'hiv_envelope.mrc',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
         ],
        'solid_levels': [
          ( 134.95980766296387, 0, ),
          ( 140.5892254257202, 0.5, ),
          ( 146.21864318847656, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.2, 0.7, 0.9333333333333333, 1.0, ),
         ],
        'surface_levels': [ 128.0, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( -0.7682877548203362, -0.28954374707755276, 0.570875068926133, ),
          'clip_plane_origin': ( 882.1725540161133, 737.9263675957918, 2271.6513061523438, ),
          'clip_thickness': 147.54983390271664,
          'display': True,
          'id': 14,
          'name': u'hiv_envelope.mrc',
          'osl_identifier': u'#14',
          'subid': 0,
          'use_clip_plane': True,
          'use_clip_thickness': False,
          'version': 4,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 121.23087465179997,
            'rotation_axis': ( -0.06788996622211037, -0.9824555167687113, 0.17370120914111448, ),
            'translation': ( 4056.118390608411, -783.5125895730275, 970.1068364749497, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.010989010457460207,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'hiv_core.mrc',
       'path': 'hiv_core.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 92, 90, 100, ),
          [ 1, 1, 1, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 92, 90, 100, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': True,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'outline_box_linewidth': 1,
          'outline_box_rgb': ( 1, 1, 1, ),
          'projection_mode': '2d-xyz',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': True,
          'two_sided_lighting': False,
          'version': 1,
          'voxel_limit': 1,
         },
        'representation': 'surface',
        'session_volume_id': u'hiv_core.mrc',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
         ],
        'solid_levels': [
          ( 130.75600146484376, 0, ),
          ( 135.82843255615234, 0.5, ),
          ( 140.90086364746094, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.8666666666666667, 0.13333333333333333, 0.06666666666666667, 1.0, ),
         ],
        'surface_levels': [ 128.0, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( -0.7682877548203362, -0.28954374707755276, 0.570875068926133, ),
          'clip_plane_origin': ( 906.8286437988281, 811.6422576904297, 2305.431396484375, ),
          'clip_thickness': 73.80314025878906,
          'display': True,
          'id': 12,
          'name': u'hiv_core.mrc',
          'osl_identifier': u'#12',
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 4,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 121.23087465179997,
            'rotation_axis': ( -0.06788996622211037, -0.9824555167687113, 0.17370120914111448, ),
            'translation': ( 4056.118390608411, -783.5125895730275, 970.1068364749497, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.010989010457460207,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
    ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')


def restore_volume_dialog():
 volume_dialog_state = \
  {
   'adjust_camera': 0,
   'auto_show_subregion': 0,
   'box_padding': '0',
   'class': 'Volume_Dialog_State',
   'data_cache_size': '128',
   'focus_volume': u'hiv_core.mrc',
   'geometry': '384x454+770+264',
   'histogram_active_order': [ 2, 1, 0, ],
   'histogram_volumes': [ u'hiv_envelope.mrc', u'hiv_debris.mrc', u'hiv_core.mrc', ],
   'immediate_update': 1,
   'initial_colors': (
     ( 0.7, 0.7, 0.7, 1, ),
     ( 1, 1, 0.7, 1, ),
     ( 0.7, 1, 1, 1, ),
     ( 0.7, 0.7, 1, 1, ),
     ( 1, 0.7, 1, 1, ),
     ( 1, 0.7, 0.7, 1, ),
     ( 0.7, 1, 0.7, 1, ),
     ( 0.9, 0.75, 0.6, 1, ),
     ( 0.6, 0.75, 0.9, 1, ),
     ( 0.8, 0.8, 0.6, 1, ),
    ),
   'is_visible': True,
   'max_histograms': '3',
   'representation': 'surface',
   'selectable_subregions': 0,
   'show_on_open': 1,
   'show_plane': 1,
   'shown_panels': [ 'Display style', 'Threshold and Color', 'Feature buttons', ],
   'subregion_button': 'button 2',
   'use_initial_colors': 1,
   'version': 12,
   'voxel_limit_for_open': '256',
   'voxel_limit_for_plane': '256',
   'zone_radius': 2.0,
  }
 from VolumeViewer import session
 session.restore_volume_dialog_state(volume_dialog_state)

try:
  restore_volume_dialog()
except:
  reportRestoreError('Error restoring volume dialog')


def restore_scale_bar():
 scale_bar_state = \
  {
   'bar_length': '1000',
   'bar_rgba': ( 1, 1, 1, 1.0, ),
   'bar_thickness': '100',
   'class': 'Scale_Bar_Dialog_State',
   'frozen_models': [ ],
   'geometry': '293x196+748+72',
   'is_visible': False,
   'label_rgba': ( 1, 1, 1, 1.0, ),
   'label_text': u'# \xc5',
   'label_x_offset': '',
   'label_y_offset': '',
   'model': None,
   'move_scalebar': 0,
   'orientation': 'horizontal',
   'preserve_position': 1,
   'screen_x_position': '0.049',
   'screen_y_position': '-0.46',
   'show_scalebar': 0,
   'version': 1,
  }
 import ScaleBar.session
 ScaleBar.session.restore_scale_bar_state(scale_bar_state)

try:
  restore_scale_bar()
except:
  reportRestoreError('Error restoring scale bar')


try:
	import Ilabel
	il = Ilabel.LabelsModel(create=False)
	if il:
		il.destroy()
	from Ilabel.Label import Label, Character
	il = Ilabel.LabelsModel()
	il.restoreSession({'labelIDs': [], 'curLabel': None, 'labels': [], 'labelUID': 0})
	del Ilabel, Label, Character, il
except:
	reportRestoreError("Error restoring IlabelModel instance in session")

ctMap = {
}

try:
	newMap = {}
	from SimpleSession import idLookup
	for k, v in ctMap.items():
		if v:
			value = [idLookup(a) for a in v]
		else:
			value = v
		newMap[idLookup(k)] = value
	# avoid having the group missing its 'chainTraceMapping' attribute
	# for any period of time...
	from chimera import PseudoBondMgr
	ctGroup = PseudoBondMgr.mgr().findPseudoBondGroup(u'missing segments')
	if hasattr(ctGroup, "chainTraceMapping"):
		needHandlers = False
	else:
		needHandlers = True
		ctGroup.chainTraceMapping = {}
	ctGroup.display = True
	# chain-trace pseudobonds only exists after a redraw...
	def restoreLBCTmap(trigName, info, trigArgs):
		ctGroup, ctMap, needHandlers = info
		try:
			from chimera import triggers, _longBondTraceCB, _chainTraceSessionCB
			from SimpleSession import SAVE_SESSION
			if needHandlers:
				ctGroup.chainTraceMapping = ctm = {}
				triggers.addHandler("Atom",
						_longBondTraceCB, ctGroup)
				triggers.addHandler(SAVE_SESSION,
						_chainTraceSessionCB, ctGroup)
			for lbpb, v in ctMap.items():
				if v:
					a1, a2 = v
					pbs1 = set(a1.pseudoBonds)
					pbs2 = set(a2.pseudoBonds)
					for pb in (pbs1 & pbs2):
						if pb.category.startswith(
						"internal-chain-"):
							value = pb
							break
					else:
						value = None
				else:
					value = v
				ctm[lbpb] = value
		finally:
			from chimera.triggerSet import ONESHOT
			return ONESHOT
	import chimera
	chimera.triggers.addHandler("post-frame", restoreLBCTmap,
						(ctGroup, newMap, needHandlers))
except:
	reportRestoreError('Error restoring chain-trace pseudobond group')


def restoreLightController():
	import Lighting
	Lighting._setFromParams({'brightness': 1.05300518926304, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 0.8613070249557495], 'quality': 'normal', 'contrast': 1.7222136572191813, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.20000000298023224]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQRhdHRycQhdcQkoVQRuYW1lcQpVBG1vZGVxC1UGZnJhbWVzcQxVDWRpc2NyZXRlRnJhbWVxDVUKZnJhbWVDb3VudHEOVQpmcmFtZVBhdXNlcQ9VDnJlc3RvcmluZ0ZyYW1lcRBVDW1pZGFzQ29tbWFuZHNxEVUKbWlkYXNGcmFtZXESVQpwcm9wZXJ0aWVzcRNlaBJLAWgNSwFoD4loC1UGbGluZWFycRRoDEsBaBFVAGgQiWgTXXEVVQNhbGxxFmFoDksBaApoBHViVQhrZXlmcmFtZXEXaAUpgXEYfXEZKGgIXXEaKGgKaAtoDGgNaA5oD2gQaBFoEmgTZWgSSxRoDUsBaA+JaAtVBmxpbmVhcnEbaAxLFGgRVQBoEIloE11xHFUDYWxscR1haA5LAWgKVQhrZXlmcmFtZXEedWJVBXNjZW5lcR9oBSmBcSB9cSEoaAhdcSIoaApoC2gMaA1oDmgPaBBoEWgSaBNlaBJLAWgNSwFoD4loC2gbaAxLAWgRVQBoEIloE11xI2gdYWgOSwFoClUFc2NlbmVxJHVidWIu'
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UFbmFtZXNxBClzYi4='
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('Margy_thin', [[0.25, 0.25], [0.4, 0.25], [0.4, 0.25], [1.5, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('FAT', [[0.6, 0.6], [1.5, 0.6], [1.5, 0.6], [3, 0.25, 0.25, 0.25], [0.7, 0.7]]), ('BS', [[0.3, 0.3], [1.5, 0.3], [1.5, 0.3], [3, 0.3, 0.25, 0.3], [1.5, 0.3]]), ('for3Dprint1', [[0.5, 0.5], [0.9, 0.5], [0.9, 0.5], [1.8, 0.5, 0.5, 0.5], [0.9, 0.5]]), ('encyclo_virol_2006_FAT', [[0.6, 0.6], [1.5, 0.6], [1.5, 0.6], [3, 0.25, 0.25, 0.25], [0.6, 0.6]]), ('Liz1', [[0.5, 0.5], [0.9, 0.25], [0.9, 0.25], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('histon_1_s1', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]]), ('minus_20%', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]), ('slimrib', [[0.2, 0.2], [1, 0.2], [1, 0.2], [0.2, 0.2, 2, 0.2], [1, 0.2]]), ('narrow nucleic 2 -gary', [[0.2, 0.2], [0.9, 0.2], [0.95, 0.2], [1.8, 0.2, 0.2, 0.2], [0.35, 0.35]]), ('plump', [[0.3, 0.3], [1.2, 0.3], [1.2, 0.3], [2, 0.3, 0.3, 0.3], [1.2, 0.3]]),
('helen2', [[0.4, 0.4], [1.7, 0.4], [2, 0.4], [2, 0.4, 0.4, 0.4], [0.9, 0.25]]), ('maya', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [1.8, 0.2, 0.2, 0.2], [0.9, 0.2]]), ('80percent', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]), ('thin even', [[0.4, 0.4], [0.4, 0.4], [0.4, 0.4], [0.4, 0.4, 0.4, 0.4], [1.5, 0.25]]), ('testdefault', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('fatz', [[0.25, 0.25], [2.5, 0.25], [2.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('user default', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.5, 0.25]]), ('default', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.5, 0.25]]), ('Margy_medium', [[0.45, 0.25], [0.7, 0.25], [0.7, 0.25], [1.5, 0.25, 0.45, 0.25], [1.5, 0.25]]), ('encyclo_virol_2006_STD', [[0.4, 0.4], [1.5, 0.4], [1.5, 0.4], [3, 0.25, 0.25, 0.25], [0.4, 0.4]]), ('thin', [[0.15, 0.15], [0.75, 0.15], [0.75, 0.15], [1.75, 0.15, 0.15, 0.15], [1.5, 0.25]]), ('aa', [[0.25, 0.25], [1.7, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.7, 0.25]]),
('slim', [[0.2, 0.2], [0.6, 0.2], [0.6, 0.2], [1, 0.2, 0.2, 0.2], [0.6, 0.2]]), ('SUPERFAT', [[0.7, 0.7], [1.6, 0.7], [1.6, 0.7], [3.1, 0.35, 0.35, 0.35], [0.7, 0.7]]), ('60%', [[0.15, 0.15], [0.9, 0.15], [0.9, 0.15], [1.8, 0.15, 0.15, 0.15], [0.9, 0.15]]), ('60_percent', [[0.15, 0.15], [0.9, 0.15], [0.9, 0.15], [2.4, 0.15, 0.15, 0.15], [0.9, 0.15]]), ('ssccmv_ribbon_scale', [[0.3, 0.3], [1.25, 0.5], [1.25, 0.5], [2.25, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('graham', [[0.25, 0.25], [1.2, 0.25], [0.9, 0.25], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('thin2', [[0.25, 0.15], [0.4, 0.15], [0.4, 0.15], [1, 0.15, 0.25, 0.15], [1.5, 0.25]]), ('spaghetti', [[0.25, 0.25], [0.25, 0.25], [0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25]]), ('tube', [[0.6, 0.6], [0.6, 0.6], [0.6, 0.6], [0.6, 0.6, 0.6, 0.6], [0.7, 0.7]]), ('old-default', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.5, 0.25]]), ('no-helix', [[0.25, 0.25], [0.25, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('thinturn', [[0.1, 0.25], [1.5, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]),
('linguini', [[0.1, 0.1], [0.1, 0.1], [0.1, 0.1], [0.1, 0.1, 0.1, 0.1], [0.1, 0.1]]), ('60percent', [[0.15, 0.15], [0.9, 0.15], [0.9, 0.15], [1.8, 0.15, 0.15, 0.15], [0.9, 0.15]]), ('flatgraham', [[0.2, 0.2], [1.1, 0.2], [0.9, 0.2], [1.8, 0.2, 0.2, 0.2], [0.9, 0.2]]), ('Liz2', [[0.35, 0.35], [0.9, 0.25], [0.9, 0.25], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('40%', [[0.1, 0.1], [0.6, 0.1], [0.6, 0.1], [1.2, 0.1, 0.1, 0.1], [0.6, 0.1]]), ('narrow nucleic - gary', [[0.2, 0.2], [0.9, 0.2], [0.95, 0.2], [1.8, 0.2, 0.2, 0.2], [0.35, 0.2]]), ('20%', [[0.05, 0.05], [0.3, 0.05], [0.3, 0.05], [0.6, 0.05, 0.05, 0.05], [0.3, 0.05]]), ('for3Dprint1round', [[0.8, 0.8], [1.5, 0.8], [1.5, 0.8], [2.4, 0.8, 0.8, 0.8], [1, 0.6]]), ('barrel', [[0.75, 0.75], [2, 0.75], [2, 0.75], [2.6, 0.75, 0.75, 0.75], [0.9, 0.25]]), ('boaz_1', [[0.25, 0.25], [2, 0.5], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('boaz_ribbons_1', [[0.25, 0.25], [1.5, 0.25], [1, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('slim2029', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]),
('skinny', [[0.25, 0.25], [0.75, 0.25], [0.75, 0.25], [1.5, 0.25, 0.25, 0.25], [1.5, 0.25]])]
	userXSections = [('', ([(4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 2), (5, 2), (4, 3)], 1, 1, 1, 10)), ('flanged', ([(0, 0), (0, 30), (3, 30), (3, 28), (27, 28), (27, 30), (30, 30), (30, 0), (27, 0), (27, 2), (3, 2), (3, 0), (0, 0)], 1, True, False, 30)), ('diamond', ([(3, 3), (0, 5), (3, 7), (7, 7), (10, 5), (7, 3)], 0, 1, 1, 10)), ('large_octagon', ([(1, 3), (1, 5), (3, 7), (5, 7), (7, 5), (7, 3), (5, 1), (3, 1)], 1, 1, 1, 8)), ('octagon', ([(4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 2), (5, 2), (4, 3)], 1, 1, 1, 10)), ('wave', ([(18, 18), (18, 19), (18, 31), (31, 31), (31, 18)], True, True, True, 50)), ('ocatagon', ([(4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 2), (5, 2), (4, 3)], 1, 1, 1, 10)), ('ibeam', ([(10, 0), (8, 0), (8, 4), (2, 4), (2, 0), (0, 0), (0, 10), (2, 10), (2, 6), (8, 6), (8, 10), (10, 10)], 0, 1, 1, 10)), ('rimmed', ([(0, 0), (0, 25), (2, 25), (2, 24), (23, 24), (23, 25), (25, 25), (25, 0), (23, 0), (23, 1), (2, 1), (2, 0), (0, 0)], 1, True, False, 25)), ('thin_round_square', ([(4, 2), (5, 2), (6, 5), (4, 3), (4, 4), (4, 5), (6, 4), (5, 4), (5, 3), (6, 3)], True, True, True, 10)),
('aitch', ([(0, 0), (0, 10), (3, 10), (3, 6), (7, 6), (7, 10), (10, 10), (10, 0), (7, 0), (7, 4), (3, 4), (3, 0), (0, 0)], 1, True, False, 10))]
	userResidueClasses = [('crazy', (u'CA', 'N', False, False, {u'C': 0.833333, u'CA': 0.5, u'N': 0.166667})), ('aa-nomain-c-o', ('C', 'O', False, False, {})), ('pguiderot', ('P', "C1'", 1, True, {"C5'": 0.5, 'P': 0.166667, 'O2P': 0.166667, 'O1P': 0.166667, 'O3P': 0.166667, "O5'": 0.333333, 'O3T': 1, "O3'": 1, 'O5T': 0})), ('aa-camain-ca-n', ('CA', 'N', False, False, {'CA': 0.5})), ('aa-camain-ca-o', ('CA', 'O', False, False, {'CA': 0.5})), ('aa-nomain-ca-o', ('CA', 'O', False, False, {})), ('aa-camain-ca-c', ('CA', 'C', False, False, {'CA': 0.5})), ('pguide', ('P', "C1'", False, True, {"C5'": 0.5, 'P': 0.166667, 'O2P': 0.166667, 'O1P': 0.166667, 'O3P': 0.166667, "O5'": 0.333333, 'O3T': 1, "O3'": 1, 'O5T': 0}))]
	residueData = []
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

def restorePalettes():
	from chimera import palettes
	palettes._restore_session({'test': ([(1, 1, 1.0, 1.0), (0.9259259259259259, 0, 1, 1.0), (0, 0, 1, 1)], 1), 'sunset': ([(1.0, 0.4980392156862745, 0.3137254901960784, 1.0), (0.0, 0.7490196078431373, 1.0, 1.0), (0.0, 0.0, 0.5019607843137255, 1.0)], 2)})
try:
	restorePalettes()
except:
	reportRestoreError('Error restoring Palettes')
geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restore_surface_capping():
 capper_dialog_state = \
  {
   'cap_offset': '0.01',
   'cap_rgba': ( 1, 1, 1, 1, ),
   'cap_style': 'solid',
   'class': 'Capper_Dialog_State',
   'color_caps': 0,
   'geometry': '223x162+625+72',
   'is_visible': False,
   'show_caps': 1,
   'subdivision_factor': '1.0',
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_capper_dialog_state(capper_dialog_state)

try:
 restore_surface_capping()
except:
 reportRestoreError('Error restoring surface capping')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {'^align53': 'align5 ; align3', '^alignInt': 'match #3:2-12.D@P #9:9240-9250.B@P ; match #4:12-19.C@P #10:12-19.B@P', '^crossfade': 'movie crossfade frames', '^match6': 'match #4:216.A,216.B,216.C,216.D,216.E,216.F@CA #0:530-535', '^movez': 'move z -20 model #4 coord #4', '^align_int': 'match #3:2-12.D@P #9:9240-9250.B@P ; match #4:12-19.C@P #10:12-19.B@P', '^delcypCA': 'del #1:.D', '^captio': '2dlabel change caption visibility hide frames 5 ; wait 15 ; 2dlabel change caption visibility show', '^aligncypA': 'matchmaker #4:.F #1', '^symcypA': 'sym #1 group #0,pn6 surf true occupancy 0.1', '^align5': 'match #3:2-12.D@P #9:9240-9250.B@P', '^title': '2dlabel change caption visibility hide frames 5 ; wait 15 ; 2dlabel change caption visibility show color black', '^sym6': 'sym #4 group #0,p6 surf true', '^align3': 'match #4:12-19.C@P #10:12-19.B@P'}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restoreMidasBase():
	formattedPositions = {'session-start': (1.60061, 2473.25, (1594.79, -469.465, 385.529), (1828.37, -1057.31), 1004.37, {(9, 0): ((1217.9395479795126, 582.4730540194105, 447.59397431878654), (0.6510367531395003, -0.41289955886796026, -0.6369184408919412, 111.40640210728078)), (0, 0): ((2027.63, -110.8, 366.306), (0.7873050298965076, 0.09983660379111758, 0.6084270231039338, 165.28300000000002)), (7, 0): ((1250.78, 534.776, 420.898), (0.9915319171481914, -0.0859177928207611, -0.09737859186310364, 73.45530000000001)), (10, 1): ((1539.85, -33.3591, 570.712), (0.2265730700551579, -0.8745692704120501, 0.42871113255514465, 134.831)), (12, 0): ((3963.0312964993304, -1406.5815008881639, 606.6263275391804), (0.1351341143660056, -0.9890812054054479, -0.058797451035073514, 119.78219063848454)), (8, 1): ((1217.94, 582.473, 447.594), (0.6510359687968233, -0.41289998021032376, -0.63691896947343, 111.40699999999998)), (6, 0): ((1525.592034189195, 27.21849242199049, 540.2198063080803), (-0.2668275093226499, 0.07057930963509905, -0.9611564083540743, 91.85395055793055)), (11, 0): ((1548.48, -22.4945, 567.887), (0.307166116480485, -0.8597823260381179, 0.40795015469880747, 138.725)), (3, 0): ((2027.63, -110.8, 366.306), (0.7873050298965076, 0.09983660379111758, 0.6084270231039338, 165.28300000000002)), (14, 0): ((3963.0312964993304, -1406.5815008881639, 606.6263275391804), (0.1351341143660056, -0.9890812054054479, -0.058797451035073514, 119.78219063848454)), (5, 0): ((1525.59, 27.2177, 540.219), (-0.26682688659184123, 0.070579170002072, -0.961156591484199, 91.85409999999999)), (2, 0): ((2027.6278384591974, -110.8009317683582, 366.30532413686683), (0.7873106089564097, 0.09983232811844596, 0.608420505314489, 165.2831847846038)), (1, 0): ((2027.63, -110.8, 366.306), (0.7873050298965076, 0.09983660379111758, 0.6084270231039338, 165.28300000000002)), (13, 0): ((3963.0312964993304, -1406.5815008881639, 606.6263275391804), (0.1351341143660056, -0.9890812054054479, -0.058797451035073514, 119.78219063848454)), (4, 0): ((2027.6272636668168, -110.80011769840814, 366.30591665920787), (0.787310307248517, 0.09983120242486457, 0.6084210804390751, 165.28326640905573))}, {(14, 0, 'Volume'): (True, 882.1725540161133, 737.9263675957918, 2271.6513061523438, -0.7682877548203362, -0.28954374707755276, 0.570875068926133, False, 147.54983390271664), (13, 0, 'Volume'): (True, 906.2431945800781, 696.9441375732422, 2264.2266235351562, -0.7682877548203362, -0.28954374707755276, 0.570875068926133, False, 101.87811279296875), (12, 0, 'Volume'): (False, 906.8286437988281, 811.6422576904297, 2305.431396484375, -0.7682877548203362, -0.28954374707755276, 0.570875068926133, False, 73.80314025878906)}, 1, (1463.061866071711, -495.7867129525016, 385.52852911647756), False, 25.0)}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreRemainder():
	from SimpleSession.versions.v54 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 1 }
	windowSize = (635, 574)
	xformMap = {}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v54 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v54 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore()
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

